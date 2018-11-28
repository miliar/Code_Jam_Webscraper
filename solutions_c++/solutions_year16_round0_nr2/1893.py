#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char str[205];
int dp[105][2];

int calc(int now,int sg)
{
    if(now==0)
        return (sg!=str[now]);
    int &ret=dp[now][sg];
    if(ret!=-1)
        return ret;
    if(sg==str[now])
        ret=calc(now-1,sg);
    else
        ret=1+calc(now-1,!sg);
    return ret;
}

void solve(int ca)
{
    scanf("%s",str);
    int len=strlen(str);
    for(int i=0;i<len;i++){
        if(str[i]=='+')
            str[i]=1;
        else
            str[i]=0;
    }
    memset(dp,-1,sizeof(dp));
    printf("Case #%d: %d\n",ca,calc(len-1,1));
    return ;
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++)
        solve(ca);
    return 0;
}
