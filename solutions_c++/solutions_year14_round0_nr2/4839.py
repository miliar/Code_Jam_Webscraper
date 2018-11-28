#include <iostream>
using namespace std;
long double mi(long double a,long double b) { return (a<b)?a:b;}
long double C,F,X;
long double pat(int n)
{
	long double time=0,speed=2;
	int i;
	for(i=0;i<n;i++)
	{
		time+=C/speed;
		speed+=F;
	}
	time+=X/speed;
	return time;
}
void solve()
{
	long double tmp1,tmp2,ans=123456789;
	cin>>C>>F>>X;
	int b,e;
	b=0;
	e=X+100;
	while(b-e>4)
	{
		int m=(b+e)/2;
		tmp1=pat(m);
		tmp2=pat(m+1);
		if(tmp1>tmp2) b=m;
		else e=m;
	}
	int i;
	for(i=b;i<=e;i++) ans=mi(ans,pat(i));
	cout<<ans<<endl;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	cout.setf(ios::fixed);
	cout.precision(8);
	for(i=1;i<=t;i++) { printf("Case #%d: ",i); solve();}
	return 0;
}