#include<iostream>
#include<iomanip>
#include<malloc.h>
using namespace std;

int main()
{
	int t,chk;
	double c,f,x,a,a1,b,b1,v;
	cin>>t;
	double* res = (double *) calloc (sizeof(double),t);
	for (int i=0;i<t;i++)
	{
		chk=0;
		v=2.0;
		cin>>c;
		cin>>f;
		cin>>x;
		if(x<=c)
		{
			res[i]=x/v;
		}
		else
		{
			b=c/v;
			b1=x/v;
			while(chk==0)
			{
			a=b;
			a1=b1;
			b=c/(f+v);
			b1=x/(f+v);
			if((a+b1)<a1)
				{
					res[i]=res[i]+a;
				}
			else
				{
					res[i]=res[i]+a1;
					chk=1;
				}
			v=f+v;
			}
		}
	}
	for(int i=0;i<t;i++)
	{
		std::cout << std::fixed;
    std::cout << std::setprecision(7);
		cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
	}
	return 0;
}
