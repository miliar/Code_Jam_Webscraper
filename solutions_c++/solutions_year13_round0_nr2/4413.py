#include <cstdio>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <time.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long LL;
#define INF 0x3f3f3f3f
#define PI acos(-1)

const int maxn = 105;

int mp[maxn][maxn];
int n, m;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

bool ok(int x, int y){
    bool f1 = true, f2 = true;
    for(int i = 1; i <= n; i++)
        if(mp[i][y] > mp[x][y]){
            f1 = false;
            break;
        }
    for(int j = 1; j <= m; j++)
        if(mp[x][j] > mp[x][y]){
            f2 = false;
            break;
        }
    if(!f1 && !f2) return false;
    return true;
}
int main(){
    #ifdef ONLINE_JUDGE
    #else
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    scanf("%d", &T);
    for(int kcase = 1; kcase <= T; kcase++){
        scanf("%d %d", &n, &m);
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++)
                scanf("%d", &mp[i][j]);

        bool flag = true;
        for(int i = 1; i <= n && flag; i++)
            for(int j = 1; j <= m; j++){
                if(!ok(i, j)){
                    flag = false;
                    break;
                }
            }
        printf("Case #%d: ", kcase);
        if(flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
