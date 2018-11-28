#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
#define LL long long

int LIM = 1000000;
bool vis[1000010];
int Q[2000010];
int S[2000010];
char s[1000];
LL n;

int main(){
    int tca; scanf("%d", &tca);
    for (int ca=1; ca<=tca; ca++){
        scanf("%lld",&n);
        if (ca % 1 == 0) {
        fprintf(stderr, "processing case %d %lld\n", ca, n);
        }
        //LIM = n;
        if (n <= 10){
            printf("Case #%d: %lld\n", ca, n);
            continue;
        }
        LL ans = -1;

        memset(vis, 0, sizeof(vis));
        Q[0] = 1;
        S[0] = 1;
        vis[1] = true;
        int qt = 1;
        for (int qh=0; qh<qt; qh++){
            int x = Q[qh];
            if (x == n){
                ans = S[qh];
                break;
            }
            if (!vis[x+1] && x+1<=LIM){
                S[qt] = S[qh]+1;
                vis[x+1]=true;
                Q[qt++] = x + 1;
            }
            sprintf(s, "%d", x);
            int len = strlen(s);
            for (int i = 0; i< len/2; i++)
                swap(s[len-1-i], s[i]);

            int y; sscanf(s, "%d", &y);
            if (y <= LIM && !vis[y]) {
                S[qt] = S[qh]+1;
                vis[y]=true;
                Q[qt++] = y;
            }

            /*
            sprintf(s, "%d", y);
            len = strlen(s);
            for (int i = 0; i< len/2; i++)
                swap(s[i-len-1], s[i]);
            sscanf(s, "%d", &y);
            if ( y <= LIM && !vis[y]) {
                S[qt] = S[qh]+1;
                vis[y]=true;
                Q[qt++] = y;
            }
            */
        }
        printf("Case #%d: %lld\n", ca, ans);
    }
    return 0;
}
