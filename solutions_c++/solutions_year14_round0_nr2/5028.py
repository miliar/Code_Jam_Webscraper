#include <iostream>
#include<cstdio>
using namespace std;
#define min(a,b) ((a) < (b) ? (a) : (b))
int main() {
	int t,l,i;
	cin>>t;
	l=t;
	while(t--)
	{
		double c,f,x,ans;
		cin>>c>>f>>x;
		ans=x/2.0;
		double a[500000];
		a[0]=x/2.0;
		if (x>c)
		{
		double r=c/2.0;
		for(i=1;i<=(int)(x/c);i++)
		{
		a[i]=min(a[i-1],r+(x/(2.0+f*i)));
		ans=min(ans,a[i]);
		r+=(c/(2.0+f*i));
		}
		}
		cout<<"Case #"<<l-t<<": ";
		printf("%.7lf\n",ans);
	}
	return 0;
}