#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;

double c,f,x;
double cal(int mid)
{
    double t=0;
    for(int i=0;i<mid;i++)
        t+=c/(2.0+i*f);
    return t+x/(2.0+mid*f);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        int l=0,r=100001,t1,t2;
        while(1)
        {
            t1=(2*l+r)/3;
            t2=(l+2*r)/3;
            if(t2-t1<2)break;
            if(cal(t1)>cal(t2))l=t1;
            else r=t2;
        }
        double fin=1e20;
        for(int i=l;i<=r;i++)
            fin=min(fin,cal(i));
        printf("Case #%d: %.7f\n",ti++,fin);
    }
    return 0;
}
