#include <iostream>
#include <sstream>
#include <vector>
#include <windows.h>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define pb push_back
#define mp make_pair
#define INF 1000000000
#define y1 tratatatatatatata

const int MOD = 1000000007;

int t, fir;
int c[55];
int a[55][55];

void solve(){
    scanf("%d",&fir);
    fir--;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            scanf("%d",&a[i][j]);
    memset(c, 0, sizeof(c));
    for (int i = 0; i < 4; ++i)
        c[a[fir][i]]++;
    int ret = 0;
    scanf("%d",&fir);
    fir--;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            scanf("%d",&a[i][j]);
    for (int i = 0; i < 4; ++i)
        if (c[a[fir][i]]) ++ret;
    if (ret == 0) printf("Volunteer cheated!\n");
    else if (ret > 1) printf("Bad magician!\n");
    else {
        for (int i = 0; i < 4; ++i)
            if (c[a[fir][i]]) printf("%d\n", a[fir][i]);
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
