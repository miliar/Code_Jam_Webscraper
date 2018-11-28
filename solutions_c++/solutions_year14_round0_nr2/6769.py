#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{int i;
	double j,c,f,x,t,n,a,b,count,temp,s;
	cin>>n;
	for(i=1;i<=n;i++)
	{   s=0;
		t=2;
	cin>>c>>f>>x;
	while(((c/t)+x/(t+f))<(x/t))	
	{
		s=s+c/t;
	    t=t+f;
		}
		s=s+x/t;
		printf("Case #%d: %0.7lf\n",i,s);
		}
	return 0;
}
