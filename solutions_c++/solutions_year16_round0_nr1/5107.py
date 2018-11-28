#include<cstdio>
#include<cmath>
#include<cstring>
#include<iostream>
#include<cctype>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const int N=100005;
const LL mod=1e9+7;
const double eps=1e-8;
bool v[15];
int tot;
void Cal(int n)
{
    do
    {
        int r=n%10;
        if(!v[r])
        {
            tot++;
            v[r]=true;
        }
        n=n/10;
    }while(n!=0);
}
int main()
{
//    freopen("test1.in","r",stdin);
//    freopen("test2.out","w",stdout);
    int T,kase=1;
    LL n;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld",&n);
        LL ans=-1,m=n;
        tot=0;
        memset(v,false,sizeof(v));
        for(int i=2;i<=100000;i++)
        {
            Cal(m);
            if(tot==10)
            {
                ans=m;
                break;
            }
            m=n*i;
        }
        printf("Case #%d: ",kase++);
        if(ans==-1)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            printf("%lld\n",ans);
        }
    }
    return 0;
}
/*


*/
