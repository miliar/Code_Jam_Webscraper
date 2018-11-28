#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<ctime>
#include<complex>
#define ft first
#define sd second
#define pb push_back
#define mkp make_pair
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)<(b)?(b):(a))
using namespace std;
typedef long long LL;
typedef pair<int,int> Pair;
const int inf=0x3f3f3f3f;
const double eps=1e-6;
const int mod=1e9+7;
const int maxn=1010;
LL n;
bool vis[15];
void run(LL a)
{
    while(a)
    {
        vis[a%10]=1;
        a/=10;
    }
}
bool ok()
{
    for(int i=0;i<=9;i++)
        if(!vis[i]) return 0;
    return 1;
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%lld",&n);
        printf("Case #%d: ",kase);
        if(!n) printf("INSOMNIA\n");
        else
        {
            memset(vis,0,sizeof(vis));
            LL m=0;
            for(int i=1;i<=1000;i++)
            {
                m+=n;
                run(m);
                if(ok())
                {
                    printf("%lld\n",m);
                    break;
                }
            }
        }
    }
}
