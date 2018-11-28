//Problem A. Standing Ovation
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;
int a[1010],t,n,sum[1010],ans;
char s[1010];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {

        ans=0;
        memset(sum,0,sizeof(sum));
        scanf("%d%s",&n,s+1);
        for(int i=1;i<=n+1;i++)
        {
            int tmp=0;
            if(sum[i-1]<i-1)
            {
                tmp=i-1-sum[i-1];
                ans+=tmp;
            }
            sum[i]+=sum[i-1]+s[i]-'0'+tmp;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
