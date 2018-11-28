#include<stdio.h>
#include<iostream>
#include<iomanip>

using namespace std;
main()
{
	double t,j,k,c,f,x,r,T,ti,y;
	int i;
	scanf("%lf",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		for(j=0,r=2;;j++)
		{
			ti=x/r;
			T=(c/r)+(x/(r+f));
			if(ti>T)
			{
				r=r+f;
			    continue;
			}
			else if(ti<=T)
			break;
		}
		for(y=0,k=0;k<j;k++)
		{
			y=y+(c/(2+(k*f)));
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<fixed<<setprecision(7)<<y+ti<<endl;
	}
}
