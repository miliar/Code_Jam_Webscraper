#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;
ll n,tmp;
bool vis[20];
int judge(ll x)
{
    while(x!=0)
    {
        if(vis[x%10]==0)
        {
            tmp++;
            vis[x%10]++;
        }
        x/=10;
    }
    if(tmp==10)
        return 0;
    return 1;
}
int main()
{
    int T,i1=1,i;
//    freopen("A-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%I64d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i1++);
            continue;
        }
        tmp=0;memset(vis,0,sizeof(vis));
        i=1;
        while(judge(i*n))i++;
        printf("Case #%d: %I64d\n",i1++,i*n);
    }

    return 0;
}
