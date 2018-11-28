#include<iostream>
#include<fstream>
#include<limits.h>
using namespace std;
double ans,m;
void solve(double c,double f,double x,double sol,double rate,int flag)
{
	if(sol>m) return;
	//cout<<"x="<<x<<" rate="<<rate<<" p="<<x/rate<<endl;
	if(flag==1)
	{
		m=(sol<m)?sol:m;
		ans=m;
		//printf("min=%f sol=%f\n",m,sol);
	}

	solve(c,f,x,sol+ (x/rate),rate,1);//not purchase
	solve(c,f,x,sol+ (c/rate),rate+f,0);//purchase
	
}
int main()
{
	int t,d=1;
	long double c,f,x,sol;
	ofstream out;
	out.open("two.txt",ios::out);
	scanf("%d",&t);
	while(t--)
	{
		//scanf("%f %f %f",&c,&f,&x);
		cin>>c>>f>>x;char car[100];
		sol=0;m=INT_MAX;
		//cout<<c<<f<<x;
		solve(c,f,x,sol,2,0);
		sprintf(car, "Case #%d: %.7f\n",d++,ans );
		out<<car;
		printf("%.7f\n",ans);
	}
	return 0;
}