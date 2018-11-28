/*Mayoor Bishnoi*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>

#define inp(n) scanf("%d",&n);
#define inp2(x,y) scanf("%d%d",&x,&y);
#define inpl(n) scanf("%lld",&n);
#define inpl2(x,y) scanf("%lld%lld",&x,&y);
#define out(n) printf("%d\n",n);
#define outl(n) printf("%lld\n",n);
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORR(i,b,a) for(int i=b-1;i>=a;i--)
#define PB(a) push_back(a)
#define C(x) printf("%d\n",x);

using namespace std;

typedef vector< int > vi;
typedef pair< int,int > pii;
typedef vector< pii > vpii;
typedef list< int > li;
typedef long long ll;
typedef unsigned long long ull;

/*int gcd(int a,int b)
{
	while(b)
		b^=a^=b^=a%=b;
	return a;
}*/

/*int mypower(int base,int index)
{
	if(index == 0)
		return 1;
	else if(index == 1)
		return base;
	int temp=mypower(base,index/2);
	temp=(temp*temp);
	if(index&1)
		return temp*base;
	else
		return temp;
}*/

double ti;

void fun(double r,double c,double f,double x,double time)
{
	double temp,temp1;
	//printf("%lf\n",ti);
	temp1=x/r;
		if((time+temp1)<ti)
			ti=time+temp1;
	temp=c/r;
	if((time+temp)>=ti)
		return;
	else
		fun(r+f,c,f,x,time+temp);
}

main()
{
	int t,num=1;
	double c,f,x;
	inp(t)
	while(t--)
	{
		ti=100010;
		scanf("%lf%lf%lf",&c,&f,&x);
		if(c>=x)
			printf("Case #%d: %0.7lf\n",num++,x/2);
		else
		{
			fun(2,c,f,x,0);
			printf("Case #%d: %0.7lf\n",num++,ti);
		}
	}
	return 0;
}