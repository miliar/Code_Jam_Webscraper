#include<bits/stdc++.h>

using namespace std;
int cnt,n,a,b,d,i,t,l,lo,mid1,mid2,hi,j;
double c,f,x,ans,tmp1,tmp2;
double req_time(int num)
{
    double res=0,rate=2;
    for(i=0;i<num;i++)
    {
        res+=(c/rate);
        rate+=f;
    }
    res+=(x/rate);
    return res;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        lo=0;
        hi=2*x;
        ans=hi;
        while(hi-lo>3)
        {
            mid1=(lo+hi)/2;
            mid2=(lo+mid1)/2;
            tmp1=req_time(mid1);
            tmp2=req_time(mid2);
            if(tmp1<tmp2)
            {
                ans=tmp1;
                lo=mid2;
            }
            else
            {
                ans=tmp2;
                hi=mid1;
            }
        }
        for(j=lo;j<=hi;j++)
        {
            ans=min(ans,req_time(j));
        }
        printf("Case #%d: %.7lf\n",l,ans);
    }
    return 0;
}
