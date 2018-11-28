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

vector<int> Y, X;

bool test(vector<vector<int> > v, int x)
{
    for (int i = 0; i < v.size(); ++i) {
        for (int j = 0; j < v[i].size(); ++j) {
            if (v[i][j] != x) continue;
            bool f1 = Y[i] == x;
            bool f2 = X[j] == x;
            if (!f1 && !f2)
                return false;
        }
    }
    return true;
}

string result(vector<vector<int> > v)
{
    X.clear();
    Y.clear();
    for (int i = 0; i < v.size(); ++i) {
        Y.push_back(*max_element(v[i].begin(), v[i].end()));
    }
    for (int i = 0; i < v[0].size(); ++i) {
        int M = 0;
        for (int j = 0; j < v.size(); ++j) {
            M = max(M, v[j][i]);
        }
        X.push_back(M);
    }
    bool f = 1;
    for (int i = 1; i < 100; ++i) {
        f&= test(v, i);
    }
    return f ? "YES" : "NO";
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
        vector<vector<int> > v(N, vector<int>(M));
        for (int n = 0; n < N; ++n) {
            for (int m = 0; m < M; ++m) {
                cin >> v[n][m];
            }
        }
        cout << "Case #" << i << ": " << result(v) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
