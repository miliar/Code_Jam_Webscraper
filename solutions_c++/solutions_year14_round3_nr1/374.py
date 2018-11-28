/*
TASK: Part Elf
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
LL d[127];
int ans=11111,tk;
bool ok;
void iSearch(LL a,LL b)
{
    tk++;
    LL x,y,z;
    x=b/2;
    if(a>=x)
    {
        //printf("%I64d %I64d %d\n",a,x,tk);
        ans=min(ans,tk);
    }
    if(a==1 && b==2)
    {
        ok=true;
        return;
    }
    iSearch(a%x,x);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
	scanf("%d",&T);
	int tt=0;
	LL x=1;
    for(i=0;x<=1000000000000LL;i++,x*=2)
        d[i]=x;
    N=i;
    while(T--)
    {
        LL a,b,c;
        scanf("%I64d/%I64d",&a,&b);
        c=__gcd(a,b);
        a/=c;   b/=c;
        tt++;
        printf("Case #%d: ",tt);
        //printf("%I64d %I64d\n",a,b);
        for(i=0;i<N;i++)
            if(b==d[i])
                break;
        k=i;
        if(b!=d[i])
            printf("impossible\n");
        else
        {
            tk=0;   ok=false;
            ans=11111;
            iSearch(a,b);
            if(!ok || ans>40) printf("impossible\n");
            else    printf("%d\n",ans);
        }
    }
}
