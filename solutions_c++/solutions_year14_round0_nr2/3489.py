#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<map>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#define f(i,a,n) for(int i=a;i<n;i++)
#define ll long long
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sd(a) scanf("%lf",&a)
#define ss(s) scanf("%s",s)
#define size 160000
using namespace std;
/*int chk(long double c,long double f,long double x,int rate,long double &old)
{
	long double sec;
	sec=old+x/rate;
	int rate2=rate+f;
	cout<<"rate2: "<<rate2<<endl;
	int rr=c/rate;
	long double sec2;
	sec2=old+rr+(x/rate2);
	cout<<"sec: "<<sec<<"\tsec2: "<<sec2<<endl;
	if(sec2<sec)
	return 1;
	else
	{
		old=sec;
	return 0;
}
	
	}*/
int main()
{

freopen("blarge.in","r",stdin);
freopen("blarge.out","w",stdout);
long double c,f,x;
long double rate;

long double sec;
int t;
si(t);
f(xx,1,t+1)
{
	int buy=0;
	sec=0;
	rate=2;
cin>>c>>f>>x;
 long double sec2=-1,old=0;
do
{
	sec=old+x/rate;
	long double rate2=rate+f;
	//cout<<"rate2: "<<rate2<<endl;
	long double rr=c/rate;

	sec2=old+rr+(x/rate2);
//	cout<<"sec: "<<sec<<"\tsec2: "<<sec2<<endl;
if(sec2<sec)
{
buy=1;
rate+=f;
old=sec2-(x/rate);
}
else
{
buy=0;
}

}
while(buy==1);


if(sec2==-1)
	printf("Case #%d: %.7Lf\n",xx,sec);
	else
	printf("Case #%d: %.7Lf\n",xx,min(sec,sec2));
}
return 0;
}
