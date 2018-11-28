#include <cassert>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(int i = 0;i < (n);++i)

long long MOD = 1000000007;

int T;
string ar[1010];

int main() {
    cin >> T;
    FOR(itest, T) {
        int n, m;
        cin >> n >> m;
        FOR(i, n)
            cin >> ar[i];
        int res = 0;
        bool ok = true;
        FOR(i, n) {
            FOR(j, m) {
                ok = true;
                if (ar[i][j] == '.')
                    continue;
                int i1 = i;
                int j1 = j;
                bool ok1 = false;
                bool ok2 = false;
                bool ok3 = false;
                bool ok4 = false;
                i1 = i;
                j1 = j+1;
                while (i1 >= 0 && i1 < n && j1 >= 0 && j1 < m) {
                    if (ar[i1][j1] != '.') {
                        ok1 = true;
                        break;
                    }
                    ++j1;
                }

                i1 = i;
                j1 = j-1;
                while (i1 >= 0 && i1 < n && j1 >= 0 && j1 < m) {
                    if (ar[i1][j1] != '.') {
                        ok2 = true;
                        break;
                    }
                    --j1;
                }

                i1 = i+1;
                j1 = j;
                while (i1 >= 0 && i1 < n && j1 >= 0 && j1 < m) {
                    if (ar[i1][j1] != '.') {
                        ok3 = true;
                        break;
                    }
                    ++i1;
                }

                i1 = i-1;
                j1 = j;
                while (i1 >= 0 && i1 < n && j1 >= 0 && j1 < m) {
                    if (ar[i1][j1] != '.') {
                        ok4 = true;
                        break;
                    }
                    --i1;
                }
                if ((ar[i][j] == '>' && !ok1) || (ar[i][j] == '<' && !ok2) || (ar[i][j] == 'v' && !ok3) || (ar[i][j] == '^' && !ok4)) {
                    ++res;
                    if (!ok1 && !ok2 && !ok3 && !ok4) {
                        ok = false;
                        break;
                    }
                }
            }
            if (!ok)
                break;
        }
        if (!ok) 
            cout << "Case #" << (itest + 1) << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << (itest + 1) << ": " << res << endl;
    }
}