#include<iostream>
#include<stdio.h>
#include<cstdio>
#include<stdlib.h>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<ctype.h>
#include<map>
#include<time.h>
#include<bitset>
#include<set>
#include<list>
using namespace std;
//gcj quali Pro A

const int maxn=10010;
int aud[maxn];
int pre[maxn];
int T;
int s;
int ans;
string a;
void solve()
{
//    if(aud[0]==0)
//    {
//        pre[1]=1;
//        ans++;
//    }
//    else
//    {
//        pre[1]=aud[0];
//    }
    pre[1]=aud[0];
    for(int i=1;i<=s;i++)
    {
        if(aud[i]==0)
        {
            pre[i+1]=pre[i];
            continue;
        }
        int level=i;
        if(pre[i]<level)
        {
            ans+=(i-pre[level]);
            pre[i+1]=pre[i]+aud[i]+(i-pre[level]);
        }
        else
        {
            pre[i+1]=pre[i]+aud[i];
        }

    }

}
int main()
{
    //freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large-output.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        ans=0;
        memset(aud,0,sizeof(aud));
        memset(pre,0,sizeof(pre));
        a="";
        scanf("%d",&s);
        cin>>a;
        int len=a.length();
        for(int i=0;i<len;i++)
        {
            aud[i]=a[i]-'0';
        }
        solve();
        printf("Case #%d: %d\n",ca,ans);
    }

    return 0;

}
