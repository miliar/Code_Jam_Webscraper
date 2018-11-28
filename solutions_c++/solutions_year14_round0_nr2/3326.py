#include<iostream>
#include<cstring>
#include<stack>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
void work()
{
	double a,b,c,f,ans,x;
	int n;
	cin>>c>>f>>x;
	ans=x/2.0;
	a=c/2.0;
	b=x/(f+2.0);
	n=1;
	while (ans>a+b)
	{
		ans=a+b;
		a+=c/(n*f+2.0);
		n++;
		b=x/(n*f+2.0);
	}
	printf("%.7lf\n",ans);
}
int main()
{
	int cas;
	int T;
	cas=0;

	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);	
	cin>>T;
	while (T--)
	{
		cas++;
		cout<<"Case #"<<cas<<": ";
		work();
	}	 
} 
