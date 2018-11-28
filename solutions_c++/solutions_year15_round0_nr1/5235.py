#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 1000+20;

int sum[maxn];
char S[maxn];
int smax;

int main() {
    int T;
    scanf("%d",&T);
    int index = 1;
    int ans = 0;
    int cnt = 0;
    while(T--) {
        scanf("%d %s",&smax,S);
        ans = cnt = 0;
        for(int i=0;i<=smax;i++) {
            if(cnt < i && S[i] > '0') {
                ans += i-cnt;
                cnt += i-cnt;
                cnt += S[i] - '0';
            }
            else {
                cnt += S[i] - '0';
            }
        }
        printf("Case #%d: %d\n",index++,ans);
    }
    return 0;
}


