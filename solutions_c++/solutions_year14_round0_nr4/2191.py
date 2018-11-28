//#pragma comment(linker, "/STACK:102400000,102400000")
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#include<cctype>
#include<string>
#include<algorithm>
#include<iostream>
#include<ctime>
#include<map>
#include<set>
using namespace std;
#define MP(x,y) make_pair((x),(y))
#define PB(x) push_back(x)
typedef long long LL;
//typedef unsigned __int64 ULL;
/* ****************** */
const int INF=1000111222;
const double INFF=1e100;
const double eps=1e-8;
const int mod=20115601;
const int NN=2005;
const int MM=401010;
/* ****************** */

double x[NN],y[NN];
bool vx[NN],vy[NN];
set<double>Mset;
set<double>::iterator itt;


// sui bian bao
int fun1(int n)
{
    int i,ans=0;
    Mset.clear();
    for(i=1;i<=n;i++)
        Mset.insert(y[i]);

    for(i=1;i<=n;i++)
    {
        itt=Mset.upper_bound(x[i]);
        if(itt==Mset.begin())
        {

        }
        else
        {
            ans++;
            itt--;
            Mset.erase(itt);
        }
    }
    return ans;
}

int fun2(int n)
{
    int i,ans=0;
    Mset.clear();
    for(i=1;i<=n;i++)
        Mset.insert(y[i]);

    for(i=1;i<=n;i++)
    {
        itt=Mset.upper_bound(x[i]);
        if(itt==Mset.end())
        {
            ans++;
        }
        else
        {
            Mset.erase(itt);
        }
    }

    return ans;
}

int main()
{
    freopen("E:\\D-large.in","r",stdin);
    freopen("E:\\D-large.out","w",stdout);

    int cas,ee=0;
    int i,n;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
            scanf("%lf",&x[i]);
        for(i=1;i<=n;i++)
            scanf("%lf",&y[i]);

        sort(x+1,x+1+n);
        sort(y+1,y+1+n);

        int ans1=fun1(n);
        int ans2=fun2(n);

        printf("Case #%d: %d %d\n",++ee,ans1,ans2);
    }
    return 0;
}
