#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

const double eps = 1e-5;
const int maxn = 10000000;
double c,f,x;

double pre[maxn],tt[maxn];

double fi()
{
    double ti = 0,sh=2.0;
    tt[0] = 0;pre[0] = x/sh;
    for(int i=1;i<maxn;i++)
    {
        tt[i] = tt[i-1] + c/(sh+(i-1)*f);
        pre[i] = tt[i] + x/(sh+i*f);
    }
}


int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        fi();
        int pt = 0;
        for(int i=1;i<maxn;i++)
            if(pre[i]<pre[pt])
                pt = i;
        printf("Case #%d: %.8lf\n",++cas,pre[pt]);
    }
}
