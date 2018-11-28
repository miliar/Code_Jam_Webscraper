#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int N=105;
const char dic[3]="+-";
char s[N];
int dp[N][2];
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%s",s);
        for(int i=0; i<2; ++i)
            dp[0][i]=i;
        if(s[0]=='-')
            swap(dp[0][0],dp[0][1]);
        int len=strlen(s);
        for(int i=1; i<len; ++i)
            for(int j=0; j<2; ++j)
                if(s[i]==dic[j])
                    dp[i][j]=min(dp[i-1][j],dp[i-1][1-j]+1);
                else
                    dp[i][j]=min(dp[i-1][j]+2,dp[i-1][1-j]+1);
        printf("Case #%d: %d\n",cas,dp[len-1][0]);
    }
    return 0;
}
