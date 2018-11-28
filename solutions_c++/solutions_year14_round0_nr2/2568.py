#include <iostream>
#include<stdio.h>
using namespace std;

int main() 
{
	long long t,k=0,a,b;
	long double c,f,x,i,j,t1,t2,t3;
	cin>>t;
	while(t--)
	{
		k++;
		cin>>c>>f>>x;
		t1=x/2;
		i=c/2;
		t2=i+x/(f+2);
		
		if(t1<t2)
		{
			printf("Case #%lld: %.7Lf\n",k,t1);
			//cout<<"Case #"<<k<<": "<<t1<<endl;
			continue;
		}
		
		j=i+c/(f+2);
		t3=j+x/(2*f+2);
		
		if(t2<t3)
		{
			printf("Case #%lld: %.7Lf\n",k,t2);
			//cout<<"Case #"<<k<<": "<<t2<<endl;
			continue;
		}
		a=1;
		b=1;
		i=c/2;
		while(1)
		{
			i+=c/(b*f+2);
			t2=i+x/((b+1)*f+2);
			
			b++;
			
			j=i+c/(b*f+2);
			t3=j+x/((b+1)*f+2);
			if(t2<t3)
			{
				printf("Case #%lld: %.7Lf\n",k,t2);
				//cout<<"Case #"<<k<<": "<<t2<<endl;
				break;
			}
			
		}
	}
	return 0;
}