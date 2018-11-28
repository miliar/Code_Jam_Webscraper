#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<set>
#include<bitset>
#include<map>
#include<stack>
#include<queue>
#include<vector>
#include<utility>
#define INF 0x3f3f3f3f
#define inf 2*0x3f3f3f3f
#define llinf 1000000000000000000
#define pi acos(-1)
#define mod 1000000007
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
typedef long long ll;
typedef pair<int,int>P;
int t,k;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("lout.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        char s[1005];int x[1005],Count=0;
        scanf("%s%d",s,&k);
        int len=strlen(s);
        for(int i=0;i<len;i++)
        {
            if(s[i]=='+')x[i]=1;
            else x[i]=0;
        }
        for(int i=0;i<=len-k;i++)
        {
            if(x[i]==0)
            {
                for(int j=i;j<i+k;j++)
                {
                    x[j]=!x[j];
                }
                Count++;
            }
        }
        int flag=1;
        for(int i=len-k+1;i<len;i++)
        {
            if(x[i]==0)
            {
                flag=0;break;
            }
        }
        if(flag)printf("Case #%d: %d\n",cas,Count);
        else printf("Case #%d: IMPOSSIBLE\n",cas);
    }
    return 0;
}
