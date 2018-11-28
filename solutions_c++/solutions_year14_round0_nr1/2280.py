#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define LL long long
using namespace std;

int vis[20];

int main(){
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("A-small-attempt0.out", "w", stdout);
    int t;
    int n1, n2, a;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; ++tt){
        memset(vis, 0, sizeof(vis));
        scanf("%d", &n1);
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                scanf("%d", &a);
                if(i == n1) ++vis[a];
            }
        }
        scanf("%d", &n2);
        int ans = 0;
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                scanf("%d", &a);
                if(i == n2){
                    ++vis[a];
                    if(vis[a] == 2){
                        if(ans == 0) ans = a;
                        else ans = -1;
                    }
                }
            }
        }
        if(ans == 0) printf("Case #%d: Volunteer cheated!\n", tt);
        else if(ans==-1) printf("Case #%d: Bad magician!\n", tt);
        else printf("Case #%d: %d\n", tt, ans);
    }
	return 0;
}
