#include<iostream>
#include <iomanip>
using namespace std;
struct numin
{
	double C,F,X;
};
int i,j;
void check(struct numin *,int);
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	struct numin a[100];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>a[i].C;
		cin>>a[i].F;
		cin>>a[i].X;
	}
	check(a,t);
	return 0;
}
void check(struct numin *a,int t)
{
	double dtn,indt,dtp;
	for(i=0;i<t;i++)
	{
		dtp=dtn=a[i].X/2;
		indt=0;
		j=0;
		while(dtn<=dtp)
		{
			indt=a[i].C/(2+j*a[i].F)+indt;
			dtp=dtn;
			dtn=a[i].X/(2+(j+1)*a[i].F)+indt;
			j++;
		}
		cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<dtp<<endl;
	}
}
