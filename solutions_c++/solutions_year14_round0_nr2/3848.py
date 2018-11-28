#include<iostream>
#include<limits.h>
#include<cstdio>
using namespace std;
int main()
{
	int t,i;
    double c,f,x,a,b,freq,check,sum;
    freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(i=1;i<=t;i++)
    {
		sum=0.0;
		freq = 2.0;
		cin>>c>>f>>x;
		sum = x/freq;
		check = 0;
		while(1)
        {
			check+= c/freq;
			freq=freq+f;
			a= x/freq;
			if(check+a<sum)
                sum = check+a;
			else
                break;
		}
		printf("Case #%d: %0.7lf\n",i,sum);
	}
	return 0;
}
