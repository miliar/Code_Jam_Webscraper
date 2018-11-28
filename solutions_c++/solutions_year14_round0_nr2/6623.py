#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
int t,k;
double c,f,x;
double c1,c2;
cin>>t;
for(k=1;k<=t;k++)
{	
	printf("Case #%d : ",k);
	c1=2.0,c2=0.0;
	cin>>c>>f>>x;
	if(x<=c)
	{
		printf("%.7lf\n",x/2);
		continue;
		}
	double ans=x/2;
	double temp=c/2;
	double time=temp+x/(2+f);
//cout<<time<<endl;
	if(time < ans)
	ans=time;
	else 
	{ printf("%.7lf\n",ans); continue; }
//cout<<ans<<endl;
	while(1)
	{
		c1+=f;
		c2=c1+f;
		temp+= c/c1;
//cout<<temp<<" ";
		time= temp + x/c2;
//cout<<time<<endl;
		if(time<ans) ans=time;
		else break;
		}
	printf("%.7lf\n",ans);
}
return 0;
}		
		
		
		
		
		
		