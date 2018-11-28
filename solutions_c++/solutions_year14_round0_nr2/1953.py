#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,i,k;
	double c,f,x,m;
	double t1,t2,tot;
	cin>>t;
	for(i=0;i<t;i++)
	{
		tot=0;
		m=2.0;
		k=0;
		cin>>c>>f>>x;
		while(k==0)
		{
			t1=x/m;
			t2=c/m+x/(m+f);
			if(t1<t2)
			{
				tot+=t1;
				k=1;
			}
			else
			{
				tot+=c/m;
				m+=f;
			}
		}
		printf("Case #%d: %.7f\n",(i+1),tot);
	}
	return 0;
}
