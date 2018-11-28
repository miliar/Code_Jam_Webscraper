//Sat Apr 12 09:05:00 IST 2014
//Author- Priyanshu Srivastava
//CSE 2nd Year
//MNNIT Allahabad

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>

#define min(a,b) 	(a<b?(a):(b))
#define max(a,b) 	(a>b?(a):(b))
#define getcx 		getchar_unlocked
#define lli 		long long
#define clr(a,b) 	memset(a,b,sizeof(a))

#define S(a) 		scanf("%d",&a);
#define SL(a) 		scanf("%lld",&a);
#define SS(a) 		scanf("%s",a);
#define SA(a,n) 	{ int i;for(i=0;i<n;i++) scanf("%d",&a[i]);   }
#define SLA(a,n) 	{ int i;for(i=0;i<n;i++) scanf("%lld",&a[i]); }
#define PA(a,n) 	{ int i;for(i=0;i<n;i++) printf("%d ",a[i]);printf("\n");  }
#define PLA(a,n) 	{ int i;for(i=0;i<n;i++) printf("%lld ",a[i]);printf("\n");}

//Bitwise
#define chkbit(s, b) 	(s & (1<<b))
#define setbit(s, b) 	(s |= (1<<b))
#define clrbit(s, b) 	(s &= ~(1<<b))

#define chk(a) 		cout << endl << #a << " : " << a << endl;
#define gc 		getchar();

using namespace std;
void fscani(int *x)
{
	int n=0;int sign=1;char c=getcx();
	while(c<'0' || c>'9'){if(c=='-') sign=-1;c=getcx();}
	while(c>='0' && c<='9'){n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
	n=n*sign;*x=n;
}
void fscanl(lli *x)
{
	lli n=0;int sign=1;char c=getcx();
	while(c<'0' || c>'9'){if(c=='-') sign=-1;	c=getcx();}
	while(c>='0' && c<='9')	{n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
	n=n*sign;*x=n;
}

void preprocess()
{
	
}

double solve(double cookies,double x,double rate,double cost,double extra )
{
	double a1,a2;
	/*if(cookies >= x)
		return 0;
	if(cookies >= cost)
		a1 = solve(cookies - cost, x, rate + extra, cost, extra);
	else
	{*/
	a2 = x / rate; 
	a1 = cost / rate;
	while(a1 < a2 && a1 + x/(rate+ extra) <=a2)
	{
		rate = rate + extra;
		a2 = a1 + x/rate;
		a1 = a1 + cost / rate;				
	}
	return a2;
}

int main()
{
	int t;S(t);int i;
	for(i=1;i<=t;i++)
	{	
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		printf("Case #%d: %0.7lf\n",i,solve(0, X, 2, C, F));
	}
	return 0; 
}
