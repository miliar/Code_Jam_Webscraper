#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<vector>
using namespace std;
long long t,n;
double v,x,r[101],c[101];
int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld",&t);
	for(int o=1; o<=t; o++)
	{
		scanf("%lld%lf%lf",&n,&v,&x);
		for(int i=1; i<=n; i++)
        {
            scanf("%lf%lf",&r[i],&c[i]);
        }
        if(n==1)
        {
            if(c[1]!=x) {printf("Case #%d: IMPOSSIBLE\n",o); continue;}
            else printf("Case #%d: %.9lf\n",o,v/r[1]);
        }
        else if(n==2)
        {
            if((c[1]<x&&c[2]<x)||(c[1]>x&&c[2]>x)) {printf("Case #%d: IMPOSSIBLE\n",o); continue;}
            if(c[1]!=c[2])
            {
                double v0=(x-c[2])*v/(c[1]-c[2]);
                double v1=v-v0;
                printf("Case #%d: %.9lf\n",o,max(v0/r[1],v1/r[2]));
            }
            else if(c[1]==x)
            {
                printf("Case #%d: %.9lf\n",o,v/(r[1]+r[2]));}
            else if(c[1]!=x) printf("Case #%d: IMPOSSIBLE\n",o);
        }
		/*(v0*c0+v1*c1)/(v0+v1)=x
		v0+v1=v
		(v0*c0+(v-v0)*c1)/v=x
		(v0*c0+v*c1-v0*c1)/v=x
		v0*(c0-c1)/v+c1=x
		v0=(x-c1)*v/(c0-c1)*/
	}
	return 0;
}
