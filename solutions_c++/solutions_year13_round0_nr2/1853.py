#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int nTests;
    cin >> nTests;

    const int N = 110;
    int a[N][N];
    
    for (int test = 0; test < nTests; ++test) {
        int n, m;
        cin >> n >> m;
        vector<int> rmax(n), cmax(m);
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> a[i][j];
                rmax[i] = max(rmax[i], a[i][j]);
                cmax[j] = max(cmax[j], a[i][j]);
            }
        }
        
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] != min(rmax[i], cmax[j])) {
                    ok = false;
                }
            }
        }
            
        cout << "Case #" << test + 1 << ": ";
        cout << (ok ? "YES" : "NO");
        cout << '\n';
    }

    return 0;
}