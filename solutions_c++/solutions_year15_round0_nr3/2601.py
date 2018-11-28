#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include <sstream>
using namespace std;

                 //1, i, j, k,-1,-i,-j,-k
int qp[8][8] = {  {0, 1, 2, 3, 4, 5, 6, 7},
                  {1, 4, 3, 6, 0, 0, 0, 0},
                  {2, 7, 4, 1, 0, 0, 0, 0},
                  {3, 2, 5, 4, 0, 0, 0, 0},
                  {0, 0, 0, 0, 0, 0, 0, 0},
                  {0, 0, 0, 0, 0, 0, 0, 0},
                  {0, 0, 0, 0, 0, 0, 0, 0},
                  {0, 0, 0, 0, 0, 0, 0, 0}};

int dleft[8][8];
int dright[8][8];


bool check(const std::vector<int>& cq_s, const std::vector<int>& cq_e, int s1, int s2) {

    if (cq_s[s1 - 1] != 1) return false;

    int aux = dleft[cq_s[s1 - 1]][cq_s.back()];
    if (dright[cq_e[s2]][aux] != 2) return false;

    if (cq_e[s2] != 3) return false;

    return true;

}

void calc(const std::string& q, std::vector<int>& cq_s, std::vector<int>& cq_e) {
    int r = 0;
    cq_s.resize(q.size());
    cq_e.resize(q.size());
    for (int i = 0; i < q.size(); ++i) {
        r = qp[r][q[i] - 'i' + 1];
        cq_s[i] = r;
    }

    r = 0;
    for (int i = (int)q.size() - 1; i >= 0; --i) {
        r = qp[q[i] - 'i' + 1][r];
        cq_e[i] = r;
    }
}

std::string repeat(const std::string& s, int n) {
    std::string sout(n*s.size(), '.');
    int idx = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < s.size(); ++j, ++idx) sout[idx] = s[j];
    return sout;
}

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");


    for (int i = 0; i < 4; ++i)
        for (int j = 4; j < 8; ++j) qp[i][j] = (qp[i][j - 4] + 4) % 8;

    for (int i = 4; i < 8; ++i)
        for (int j = 0; j < 8; ++j) qp[i][j] = (qp[i - 4][j] + 4) % 8;

    for (int i = 0; i < 8; ++i)
        for (int j = 0; j < 8; ++j) {
            dleft[i][qp[i][j]]  = j;
            dright[j][qp[i][j]] = i ;
        }

    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        int l, x;
        std::string q;
        fin >> l >> x >> q;
        std::cout << l << " " << x << std::endl;
        q = repeat(q, x);

        std::cout << q.size() << std::endl;
        std::vector <int> cq_s, cq_e;
        calc(q, cq_s, cq_e);

        bool found = false;
        for (int i = 1; i  < q.size(); ++i) {
            for (int j = i + 1; j < q.size(); ++j) {
                if (check(cq_s, cq_e, i, j)) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        fout << "Case #" << test_case << ": " << (found ? "YES" : "NO") << endl;
    }

    fin.close();
    fout.close();

}

