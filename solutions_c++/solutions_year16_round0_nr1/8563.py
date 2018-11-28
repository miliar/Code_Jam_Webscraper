#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	long long t;
	cin>>t;
	long long n[t];
	long long result[t];
	long long number=0;
	long long x;
	long long p;
	long long asdf[11];
	long int temp=0;
	while(temp<t)
	{
		cin>>n[temp];
		temp++;
	}
	temp=0;
	while(temp<t)
	{
		number=0;
		int m=0;
		while(m<11)
		{
			asdf[m]=-1;
			m++;
		}
		if(n[temp]==0)
		{
			result[temp]=0;		
			temp++;
			continue;
		}
		int z=1;
		while(1)
		{
			x=z*n[temp];
			while(1)
			{
				p=x;
				p=p%10;
				int ap=0;
				while(ap<11)
				{
					if(p==asdf[ap])
					{
						break;
					}
					ap++;
				}
				if(ap==11)
				{
					asdf[number]=p;
					number++;		
				}
				x=x/10;
				if(x==0)
				{
					break;
				}			
			}
			if(number==10)
			{
				result[temp]=z*n[temp];
				break;
			}
			z++;	
		}
		temp++;
	}
	temp=0;
	while(temp<t)
	{
		if(result[temp]==0)
		{
			cout<<"case #"<<(temp+1)<<": "<<"INSOMNIA"<<endl;	
		}
		else
		{
			cout<<"case #"<<(temp+1)<<": "<<result[temp]<<endl;
		}
		temp++;
	}
	return 0;
}