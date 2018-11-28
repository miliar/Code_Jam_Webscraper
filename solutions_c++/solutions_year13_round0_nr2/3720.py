#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Lawn {
public:
    Lawn(vector<vector<int> >, int, int);
    ~Lawn();
    bool judge();

private:
    vector<vector<int> > pattern;
};

Lawn::Lawn(vector<vector<int> > a, int n, int m) {
    pattern.resize(n);
    for (int i = 0; i < n; i++) {
        pattern[i].resize(m);
        for (int j = 0; j < m; j++) {
            pattern[i][j] = a[i][j];
        }
    }
}

Lawn::~Lawn()
{
}

bool Lawn::judge() {/*jjjjj
    for (int i = 1; i < pattern.size() - 1; i++) {
        for (int j = 1; j < pattern[0].size() - 1; j++) {
            if ((pattern[i][j] < pattern[i + 1][j] || pattern[i][j] < pattern[i - 1][j]) && (pattern[i][j] < pattern[i][j + 1] || pattern[i][j] < pattern[i][j - 1]))
                return false;
        }
    }
*/
    for (int i = 0; i < pattern.size(); i++) {
        int max = pattern[i][0];
        for (int j = 1; j < pattern[0].size(); j++) {
            if (pattern[i][j] > max)
                max = pattern[i][j];
        }

        for (int j = 0; j < pattern[0].size(); j++) {
            if (pattern[i][j] < max) {
                for (int k = 0; k < pattern.size(); k++) {
                    if (pattern[k][j] > pattern[i][j])
                        return false;
                }
            }
        }
    }

    return true;
}

int main()
{
    ifstream inf("B-large.in");
//    ifstream inf("small.in");
    ofstream of("result.out");

    int T;

    inf >> T;
    int S = T;
    //pretreatment
    
    while (T > 0) {
        int M,N;
        inf >> N;
        inf >> M;
        vector<vector<int> > A(N, vector<int>(M));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int tmp;
                inf >> tmp;
                A[i][j] = tmp;
            }
        }

        of << "Case #" << S - T + 1 << ": ";
        Lawn l(A, N, M);
        if (l.judge())
            of << "YES\n";
        else
            of << "NO\n";

        T--;
    }

    inf.close();
    of.close();

    return 0;
}
