#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

#define epr(...) fprintf(stderr, __VA_ARGS__)
const int maxn = -1;
const int inf = 1e9;

bool use[100];
int a[4][4];


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
     freopen("out", "w", stdout);
#endif
    int t, x;
    scanf("%d", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        int n = 4;
        for (int i = 0; i < n * n; i++)
            use[i] = 1;
        for (int q = 0; q < 2; q++) {
            scanf("%d", &x); x--;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    scanf("%d", &a[i][j]);
                    a[i][j]--;
                    if (x != i)
                        use[a[i][j]] = 0;
                }
        }
        int cnt = 0;
        for (int i = 0; i < n * n; i++)
            cnt += use[i];
        if (cnt == 0) {
            printf("Volunteer cheated!\n");
            continue;
        }
        if (cnt > 1) {
            printf("Bad magician!\n");
            continue;
        }
        for (int i = 0; i < n * n; i++)
            if (use[i]) {
                printf("%d\n", i + 1);
            }
    }



    return 0;
}

