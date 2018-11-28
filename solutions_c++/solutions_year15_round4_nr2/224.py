#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
const int N=200;
int n;
double r[N],c[N];
double V,X;
bool check(double x)
{
	double sumV=0,sumX=0;
	for(int i=0;i<n;++i)
	{
		if(sumV+r[i]*x<V)
		{
			sumV+=r[i]*x;
			sumX+=r[i]*c[i]*x;
		}
		else{
			sumX+=(V-sumV)*c[i];
			sumV=V;
			if(c[i]<=X)
				sumX=0;
			break;
		}
	}
	//printf("%.10lf %.10lf %.10lf %.10lf\n",x,sumV,sumX,X*sumV);
	if(sumV<V || sumX>=X*sumV)
		return false;
	sumV=sumX=0;
	for(int i=n-1;i>-1;--i)
	{
		if(sumV+r[i]*x<V)
		{
			sumV+=r[i]*x;
			sumX+=r[i]*c[i]*x;
		}
		else{
			sumX+=(V-sumV)*c[i];
			sumV=V;
			if(c[i]>=X)
				sumX=1e15;
			break;
		}
	}
	//printf("%.10lf %.10lf %.10lf %.10lf\n",x,sumV,sumX,X*sumV);
	if(sumV<V || sumX<=X*sumV)
		return false;
	return true;
}
void work(int Case)
{
	double sumR=0;
	scanf("%d%lf%lf",&n,&V,&X);
	for(int i=0;i<n;++i)
	{
		scanf("%lf%lf",&r[i],&c[i]);
		sumR+=r[i];
	}
	for(int i=0;i<n;++i)
		for(int j=0;j+i+1<n;++j)
			if(c[j]>c[j+1])
			{
				double tmp=c[j];
				c[j]=c[j+1];
				c[j+1]=tmp;
				tmp=r[j];
				r[j]=r[j+1];
				r[j+1]=tmp;
			}
	printf("Case #%d: ",Case);
	for(int i=1;i<n;++i)
		if(c[i]==c[0])
		{
			r[0]+=r[i];
			r[i]=0;
			if(i==n-1)
				n=1;
		}
	for(int i=n-2;i>-1;--i)
		if(c[i]==c[n-1])
		{
			r[n-1]+=r[i];
			r[i]=0;
		}
	//for(int i=0;i<n;++i)
		//printf("%.10lf %.10lf\n",c[i],r[i]);
	if(c[0]==X)
	{
		printf("%.7lf\n",V/r[0]);
		return;
	}
	if(c[n-1]==X)
	{
		printf("%.7lf\n",V/r[n-1]);
		return;
	}
	if(c[0]>X || c[n-1]<X)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	double l=0,r=1000000000,mid;
	while(r-l>1e-7)
	{
		mid=(l+r)*0.5;
		if(check(mid))
			r=mid;
		else l=mid;
	}
	printf("%.7lf\n",l);
	
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
		work(i+1);
	return 0;
}