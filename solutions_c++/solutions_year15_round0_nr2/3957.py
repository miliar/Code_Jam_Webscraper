#include <iostream>
#include <vector>
#include <list>
#include <fstream>
using namespace std;


/*int solve(std::vector<int>& p) {
    int res = 123456789;
    int div_cnt = 0;
    int k = 1000;


    while (1) {
        while (k > 1 && p[k] == 0) k--;
        if (div_cnt + k < res) res = div_cnt + k;
        if (k == 1) break;

        div_cnt++;
        p[k/2]++; p[k/2 + k%2]++;
        p[k]--;
    }

    return res;
}*/

int solve(const std::vector<int>& p) {

    int m_idx = 0;
    for (int i = 1; i < p.size(); ++i) {
        if (p[i] > p[m_idx]) m_idx = i;
    }

    if (p[m_idx] <= 3) return p[m_idx];


    std::vector<int> p_split(p.size() + 1);
    int idx = 2;
    for (int i = 0; i < p.size(); ++i)
        if (i != m_idx) {
            p_split[idx] = p[i];
            idx++;
        }


    int res = p[m_idx];
   /* for (int k = 1; k <= p[m_idx]/2; ++k) {
        p_split[0] = k;
        p_split[1] = p[m_idx] - k;
        res = min(res, solve(p_split) + 1);
    }*/


    int k = p[m_idx]/2;
    p_split[0] = k;
    p_split[1] = p[m_idx] - k;
    res = min(res, solve(p_split) + 1);


    if (p[m_idx] == 9) {
        p_split[0] = 3;
        p_split[1] = 6;
        res = min(res, solve(p_split) + 1);
    }


    return res;
}

int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("B-small-attempt1.out");


    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        std::cout << "test " << test_case << std::endl;
        int d;
        fin >> d;
        std::vector<int> p(d, 0);

        /*std::vector<int> p(1001, 0);

        for (int i = 0; i < d; ++i) {
            int pp; fin >> pp; p[pp]++;
        } */

        for (int i = 0; i < d; ++i) {
            fin >> p[i];
            std::cout << p[i] << " ";
        }
        std::cout << endl;

        fout << "Case #" << test_case << ": " << solve(p) << endl;
        cout << "Case #" << test_case << ": " << solve(p) << endl;
    }

    fin.close();
    fout.close();

}

