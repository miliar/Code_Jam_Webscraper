#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 1001;

double ans[size], p[size], res[size][size];
int tc, n, k;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;

    for (int tnum = 0; tnum < tc; tnum++) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) 
            cin >> p[i];
        sort(p, p + n);

        /* 
        double rans = 0.0;
        
        for (int msk = 0; msk < (1 << n); msk++) {
            if (__builtin_popcount(msk) != k)
                continue;

            int cur = 0;
            for (int j = 0; j < n; j++) 
                if ((msk >> j) & 1) {
                    ans[cur++] = p[j];    
                }

            for (int i = 0; i <= n; i++)
                for (int j = 0; j <= n; j++)
                    res[i][j] = 0.0;

            res[0][0] = 1.0;
            for (int i = 0; i < k; i++)
                for (int j = 0; j <= i; j++) {
                    res[i + 1][j + 1] += res[i][j] * ans[i];
                    res[i + 1][j] += res[i][j] * (1 - ans[i]);
                }
            
            rans = max(rans, res[k][k / 2]);
        }
        printf("Case #%d: %.10lf\n", tnum + 1, rans);
        
        */
              
        double rans = 0.0;
        for (int h = 0; h <= k; h++) {
                for (int t = 0; t < h; t++) {
                    ans[t] = p[t];
                }
                for (int t = 0; t < n - h; t++)
                    ans[h + t] = p[n - 1 - t]; 
    
                for (int i = 0; i <= n; i++)
                    for (int j = 0; j <= n; j++)
                        res[i][j] = 0.0;

                res[0][0] = 1.0;
                for (int i = 0; i < k; i++)
                    for (int j = 0; j <= i; j++) {
                        res[i + 1][j + 1] += res[i][j] * ans[i];
                        res[i + 1][j] += res[i][j] * (1 - ans[i]);
                    }

                rans = max(rans, res[k][k / 2]);
            
        }

        printf("Case #%d: %.10lf\n", tnum + 1, rans);
        
//        cout.precision(20);
//        cout << "Case #" << tnum + 1 << ": " << res[k][k / 2] << endl;
    }

    return 0;
}