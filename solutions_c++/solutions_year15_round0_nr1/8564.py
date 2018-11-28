#include<cstdio>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#include<string.h>
#include<set>
#define eps 1e-9
#define nn 1000005
#define INF 0x7FFFFFFF

typedef __int64 LL;

using namespace std;

/*-----------------------------never more!---------------------------*/

char s[1005];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.in","w",stdout);
    int t;
    while(scanf("%d",&t)!=EOF)
    {
        int i,j;
        for(i=1;i<=t;i++)
        {
            int n,ans=0,peo=0;
            scanf("%d",&n);
            scanf("%s",s);
            for(j=0;j<=n;j++)
            {
                if(peo>=j)
                    peo+=s[j]-'0';
                else
                {
                    ans+=j-peo;
                    peo=j+s[j]-'0';
                }
            }
            printf("Case #%d: %d\n",i,ans);
        }
    }
    return 0;
}
