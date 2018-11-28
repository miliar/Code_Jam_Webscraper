#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	long long T;
	cin>>T;
	long long N[T];
	long long  result[T];
	long long number=0;
	long long x;
	long long p;
	long long check[11];
	long int temp=0;
	while(temp<T)
	{
		cin>>N[temp];
		temp++;
	}
	temp=0;
	while(temp<T)
	{
		number=0;
		int m=0;
		while(m<11)
		{
			check[m]=-1;
			m++;
		}
		if(N[temp]==0)
		{
			result[temp]=0;		
			temp++;
			continue;
		}
		int z=1;
		while(1)
		{
			x=z*N[temp];
			while(1)
			{
				p=x;
				p=p%10;
				int ap=0;
				while(ap<11)
				{
					if(p==check[ap])
					{
						break;
					}
					ap++;
				}
				if(ap==11)
				{
					check[number]=p;
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
				result[temp]=z*N[temp];
				break;
			}
			z++;	
		}
		temp++;
	}
	temp=0;
	while(temp<T)
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