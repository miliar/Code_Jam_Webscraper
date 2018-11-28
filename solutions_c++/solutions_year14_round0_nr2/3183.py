#include<algorithm>
#include<iostream>
#include<string.h>
#include<sstream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
//#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-8;
const double PI=acos(-1.0);
const int maxn=100010;
//typedef __int64 ll;

int main()
{
    int t,cas=1;
    double c,f,x,ans,now,rate;
    freopen("B-large.in","r",stdin);
    freopen("out,out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        now=0,ans=INF,rate=2;
        while(now<ans)
        {
            ans=min(ans,now+x/rate);
            now+=c/rate;
            rate+=f;
        }
        printf("Case #%d: %.7lf\n",cas++,ans);
    }
    return 0;
}
