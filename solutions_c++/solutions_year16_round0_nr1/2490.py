#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;

int n;
bool vis[30];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        if(!n) {
            puts("INSOMNIA");
            continue;
        }
        memset(vis, 0, sizeof(vis));
        for(ll i=n; ; i+=n) {
            ll t = i;
            while(t) {
                vis[t%10] = 1;
                t /= 10;
            }
            bool flag = true;
            for(int j = 0; j <= 9; j++) if(!vis[j]) {
                flag = false;
            }
            if(!flag) continue;
            cout << i << endl;
            break;
        }
    }
    return 0;
}
