#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 1000000000
#define eps 1e-8
#define lld long long
#define mem(a,b) memset((a),(b),sizeof((a)))
using namespace std;


int main() {
    int T,x,i,j,cas=0;
    int a[20][20];
    int v[20];
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--) {
        scanf("%d", &x);
        mem(v,0);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &a[i][j]);
        for(i = 1; i <= 4; i++)
            v[a[x][i]]++;
        scanf("%d", &x);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &a[i][j]);
        for(i = 1; i <= 4; i++)
            v[a[x][i]]++;
        int ans = -1, ret = 0;
        for(i = 1; i <= 16; i++)
        if (v[i] == 2){
            ans = i;
            ret++;
        }
        printf("Case #%d: ", ++cas);
        if (ans == -1) puts("Volunteer cheated!"); else
            if (ret > 1) puts("Bad magician!"); else printf("%d\n", ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
