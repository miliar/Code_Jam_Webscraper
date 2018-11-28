#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

typedef long long lint;
const int Z = 1000002013;

int result(int N, int M, const vector<int>& o, const vector<int>& e, const vector<int>& p)
{
    int res = 0;
    int v0[101][101] = {0};
    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (o[j] != i) continue;
            v0[o[j]][e[j]]+= p[j];
        }
        for (int j = 1; j < 101; ++j) {
            for (int k = j + 1; k < 101; ++k) {
                int& n1 = v0[j][k];
                if (!n1) continue;
                for (int a = j + 1; a <= k; ++a) {
                    for (int b = k + 1; b < 101; ++b) {
                        int& n2 = v0[a][b];
                        if (!n2) continue;
                        int m = min(n1, n2);
                        n1-= m;
                        n2-= m;
                        v0[j][b]+= m;
                        v0[a][k]+= m;
                        lint price = lint(a - j) * (b - k);
                        price*= m;
                        res+= price % Z;
                    }
                }
            }
        }
    }
    return res;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int N, M;
        cin >> N >> M;
        vector<int> o(M), e(M), p(M);
        for (int j = 0; j < M; ++j)
            cin >> o[j] >> e[j] >> p[j];

        cout << "Case #" << i << ": " << result(N, M, o, e, p) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
