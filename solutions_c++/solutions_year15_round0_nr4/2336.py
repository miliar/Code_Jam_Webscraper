#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<deque>
#include<time.h>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
#define cl(x,v); memset(x,v,sizeof(x));
#define llINF 1ll<<60
#define INF 1<<29
#define EPS 1e-8
#define MID int mid=(l+r)>>1; int ls=o<<1; int rs=o<<1|1;
#define pii pair<int,int>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define pss pair<short,short>
#define F first
#define S second
#define PB push_back
#define BR puts("");
#define SCn scanf("%d",&n)
#define SCnm scanf("%d%d",&n,&m)
#define rep(i,s,n) for(int i=(s);i<=(n);++i)
#define rrep(i,s,n) for(int i=(s);i>=(n);--i)
#define TSC int T; scanf("%d",&T);
#define PI acos(-1.0)
#define test printf("test\n");
#define db double
typedef unsigned long long ull;
typedef long long ll;
int x,r,c;
int tt,ii;

int main()
{
    scanf("%d",&tt);
    for(ii=1;ii<=tt;ii++)
    {
        scanf("%d %d %d",&x,&r,&c);
        int ma=max(r,c);
        int mi=min(r,c);
        int tag=0;
        if(x==1)
        {
            tag=1;
        }
        else if(x==2)
        {
            if(r%2==0||c%2==0)
            {
                tag=1;
            }
        }
        else if(x==3)
        {
            if(mi==2&&ma==3)tag=1;
            if(mi==3&&ma==3)tag=1;
            if(ma==4&&mi==3)tag=1;
        }
        else if(x==4)
        {
            if((mi==4&&ma==4)||(ma==4&&mi==3))tag=1;
        }
        printf("Case #%d: ",ii);
        if(tag==1)printf("GABRIEL\n");
        else printf("RICHARD\n");
    }
    return 0;
}
