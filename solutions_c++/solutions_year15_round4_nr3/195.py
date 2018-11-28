#include<cmath>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct num
{
     double v,x;
}a[100001];
inline bool cmp(num x,num y)
{
     if(x.x>y.x)
          return true;
     return false;
}
double eps=0.00000001;
int main()
{
//	 freopen("B-small-attempt5.in","r",stdin);
//	 freopen("B-small-attempt5.out","w",stdout);
//	 freopen("B-large.in","r",stdin);
//	 freopen("B-large.out","w",stdout);
     int T,k=0;
	 scanf("%d",&T);
	 while(T>0)
	 {
	      T--;
	      k++;
	      printf("Case #%d: ",k);
	      int n;
	      scanf("%d",&n);
	      double v,x;
	      scanf("%lf%lf",&v,&x);
	      int i;
	      for(i=1;i<=n;i++)
	           scanf("%lf%lf",&a[i].v,&a[i].x);
	      sort(a+1,a+1+n,cmp);
	      double l=0,r=1000000,mid,midx;
	      while(l+eps<r)
	      {
	           mid=(l+r)/(double)2;
	           double t1=0,t2=0;
	           double v1=0,v2=0,vl=0,tvl;
	           for(i=1;i<=n;i++)
	           {
	                v1+=a[i].v;
	                tvl=vl;
					vl+=a[i].v*mid;
	                if(v1*mid>v)
	                {
	                	 double vt=v-tvl;
	                	 t1=(tvl*t1+vt*a[i].x)/(tvl+vt);
	                     break;
	                }
	                t1=(tvl*t1+a[i].v*mid*a[i].x)/(tvl+a[i].v*mid);
	           }
	           vl=0;
	           for(i=n;i>=1;i--)
	           {
	                v1+=a[i].v;
	                tvl=vl;
	                vl+=a[i].v*mid;
	                if(vl>v)
	                {
	                	 double vt=v-tvl;
	                	 t2=(tvl*t2+vt*a[i].x)/(tvl+vt);
	                     break;
	                }
	                t2=(tvl*t1+a[i].v*mid*a[i].x)/(tvl+a[i].v*mid);
	           }
	           if(t1<x||t2>x)
	                l=mid;
	           else
	                r=mid;
	      }
	      printf("%.7lf\n",l);
	 }
	 return 0;
}
