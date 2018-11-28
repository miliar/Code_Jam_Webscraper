#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	long T;
	cin>>T;
	char data[T][110];
	int countLength;
	long result[T];
	long countFlips=0;
	int temp=0;
	while(temp<T)
	{
		cin>>data[temp];
		temp++;
	}
	temp=0;
	while(temp<T)
	{
		countFlips=0;
		while(1)
		{
			long z=(unsigned)strlen(data[temp])-1;	
			while(z>=0)
			{
				if(data[temp][z]=='+')
				{
					z--;
				}
				else
				{
					break;
				}
			}
			if(z==-1)
			{
				break;
			}
			while(z>=0)
			{
				if(data[temp][z]=='+')
				{
					data[temp][z]='-';
				}
				else
				{
					data[temp][z]='+';
				}
				z--;
			}
			countFlips++;
		}
		result[temp]=countFlips;
		temp++;
	}
	temp=0;
	while(temp<T)
	{
		cout<<"case #"<<(temp+1)<<": "<<result[temp]<<endl;
		temp++;
	}
	return 0;
}