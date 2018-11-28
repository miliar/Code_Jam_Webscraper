#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <cassert>
using namespace std;

typedef long long int64;
typedef multiset<int>::iterator msii;
#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)
#define PROBLEM "A"

const int MAXN = 10100;

int a[MAXN];
bool mark[MAXN];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int t = 1; t <= T; t++) {
        cerr << t << endl;
        printf("Case #%d: ", t);

        int n, x;
        scanf("%d %d", &n, &x);
        
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        
        stable_sort(a, a+n);
        memset(mark, 0, sizeof(mark));
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!mark[i]) {
                mark[i] = true;
                int v = a[i];
                ans++;
                
                int l = i+1, r = n-1;
                int best = -1;
                while (l <= r) {
                    int m = (l + r) / 2;
                    if (a[m] <= x - v) {
                        best = m;
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
                
                assert(best == -1 || i < best && best < n);
                if (best != -1) {
                    if (!mark[best]) {
                        mark[best] = true;
                    } else {
                        while (best > i && mark[best]) {
                            best--;
                        }
                        if (!mark[best]) {
                            assert(i < best && best < n);
                            assert(a[best] + v <= x);
                            mark[best] = true;
                        }
                    }
                }
            }
        }
        
//         multiset<int> ss;
//         for (int i = 0; i < n; i++) {
//             ss.insert(a[i]);
//         }
//         int ans = 0;
//         while (ss.size() > 0) {
//             msii it = ss.begin();
//             int v = *it;
//             msii jt = ss.lower_bound(x - v);
//             if (jt == ss.end()) {
//                 ans++;
//                 msii.remove(it);
//             } else {
//                 int w = *jt;
//                 if (w == x - v) {}
//                 msii.remove(it);
//                 msii.remove(jt);
//             }
//         }
        
        printf("%d", ans);
        printf("\n");
    }

    return 0;
}
