#include<cstdio>
#include<cstring>

using namespace std;

char s[105];
int n,dp[2][105];

void init(){
    int i,j;
    dp[0][1] = 0;dp[1][1] = 1;
    for(i = 2;i <= 100;i++){
        dp[0][i] = (i&1)?dp[0][i-1]:(dp[1][i-1]+1);
        dp[1][i] = (i&1)?(dp[0][i-1]+1):dp[1][i-1];
    }
}

int main(){
    int i,j,cas;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    init();
    for(int T=1;T<=cas;T++){
        scanf("%s",s);
        int len = strlen(s);
        int cnt = 1;
        for(i = 1;i < len;i++){
            if(s[i]!=s[i-1]) cnt++;
        }
        printf("Case #%d: %d\n",T,dp[(s[0]!='+')][cnt]);
    }

    return 0;
}
