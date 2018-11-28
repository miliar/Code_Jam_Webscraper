#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#define N 20
#define eps 1e-7
#define MIN(a,b) ((a)<(b)?(a):(b))
using namespace std;
int sign(double d)
{
    return d < -eps ? -1 : (d > eps ? 1 : 0);
}
double getvalue(int k,double c,double f,double x)
{
    int i;
    double a_time=0;
    for(i=0;i<k;i++)
        a_time+=(c/(2.0+i*f));
    return a_time+x/(2.0+k*f);
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B_out","w",stdout);
    int T;
    double c,f,x;
    scanf("%d",&T);
    int cas;
    for(cas=1;cas<=T;cas++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        int i;
        double left=0.0,right=100000.0;
        double mid,rmid;
        for(i=0;i<100;i++)
        {
            mid = (left+right)/2.0;
            rmid = (mid+right)/2.0;
            if(getvalue(mid,c,f,x)>getvalue(rmid,c,f,x))
                left = mid;
            else 
                right = rmid;
        }
        int k = mid;
        double ans_time = getvalue(k,c,f,x);
        ans_time = MIN(ans_time,getvalue(k+1,c,f,x));
        if(k>0)
        ans_time = MIN(ans_time,getvalue(k-1,c,f,x));
        printf("Case #%d: %.7lf\n",cas,ans_time);
    }
}
