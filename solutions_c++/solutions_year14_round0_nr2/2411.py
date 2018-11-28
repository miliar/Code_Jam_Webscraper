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

int main()
{
    freopen("E:\\B-large.in","r",stdin);
    freopen("E:\\B-large.out","w",stdout);

    int cas,ee=0;
    double c,f,x,i,t,ge,ans;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);

        ans=x/2.0;
        t=0.0;
        ge=0.0;

        for(i=0.0;i<200001.0;i+=1.0)
        {
            t+=c/(2.0+i*f);
            ge+=1.0;
            ans=min(ans,t+x/( 2.0 + ge*f ) );
        }

        printf("Case #%d: ",++ee);
        printf("%.10lf\n",ans);
    }
    return 0;
}
