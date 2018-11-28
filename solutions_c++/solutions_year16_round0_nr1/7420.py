#include <iostream>
using namespace std;

int main (void)
{
	int T;
	long n[100];
	long a,b;

	cin>>T;
	for(unsigned i=0;i<T;i++)
	{cin>>n[i];}
	bool set[10];
	bool token;


	for(unsigned _case=0;_case<T;_case++)
	{
		for(unsigned i=0;i<10;i++)
			{set[i]=false;}
		if(n[_case]==0)
			{
				cout<<"Case #"<<(_case+1)<<": INSOMNIA"<<endl;
			}
		else
		{
			b=n[_case];
			while(1)
			{
				a=n[_case];
				while(a>0)
				{
					set[(a%10)]=true;
					a=a/10;
				}
				token=true;
					for(unsigned i=0;i<10;i++)
						{if(set[i]==false)
							{
								token=false;
								break;
							}
						}
				if(token==true)
				{
					cout<<"Case #"<<(_case+1)<<": "<<n[_case]<<endl;
					break;
				}
				n[_case]=n[_case]+b;
			}
		}
	}
}
