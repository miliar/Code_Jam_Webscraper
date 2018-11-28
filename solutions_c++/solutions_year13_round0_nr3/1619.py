#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

const int N=10010;
double ans[50]={0};
int n;

int glen(double i)
{
	int ret = 0;
	for(;i>=1;i/=10,ret++) ;
	return ret;
}

void makefair(int i,double f[])
{
	int len=glen(i);
	int j,k;
	f[0]=i*pow(10.0,(double)len-1);
	f[1]=i*pow(10.0,(double)len);
	for(j=i/10,k=len-1;j;j/=10,k--)
		f[0]+=j%10*pow(10.0,(double)k-1);
	for(j=i,k=len;j;j/=10,k--)
		f[1]+=j%10*pow(10.0,(double)k-1);
}

bool isfair(double x)
{
	int len=glen(x);
	double y=x;
	int front,tail,i,j; 
	for(i=1,j=len;i<j;i++,j--)
	{
		tail=x-floor(x/10.0)*10;
		front=y/pow(10.0,(double)j-1);
		if(front!=tail) return 0;
		x/=10;
		y=y-front*pow(10.0,(double)j-1);
	}
	return 1;
} 

int bsrch(double key,int l,int r,int v)
{
	if(l>=r)
		return l;
	int m=(l+r)/2;
	if(key<ans[m]) return bsrch(key,l,m,v);
	else if(fabs(key-ans[m])<1e-6) return m+v;
	return bsrch(key,m+1,r,v);
}

int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("3.out","w",stdout);
	
	int i,j;
	double fair[2],pw[2];
	for(i=1,j=0;i<N;i++)
	{
		makefair(i,fair);
		pw[0]=pow(fair[0],2.0);
		pw[1]=pow(fair[1],2.0);
		if(isfair(pw[0])) ans[j++]=pw[0];
		if(isfair(pw[1])) ans[j++]=pw[1];
	}
	n=j;
	sort(ans,ans+n);
	//for(i=0;i<n;i++)
	//	printf("%d %lf\n",i,ans[i]);
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		double a,b;
		scanf("%lf%lf",&a,&b);
		int l = bsrch(a,0,n-1,0);
		int r = bsrch(b,0,n-1,1);
		printf("Case #%d: %d\n",cnt,r-l);
	}
}
