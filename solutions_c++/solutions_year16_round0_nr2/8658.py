#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	long t;
	cin>>t;
	char record[t][110];
	int countLength;
	long result[t];
	long numberOfFlips=0;
	int temp=0;
	while(temp<t)
	{
		cin>>record[temp];
		temp++;
	}
	temp=0;
	while(temp<t)
	{
		numberOfFlips=0;
		while(1)
		{
			long z=(unsigned)strlen(record[temp])-1;	
			while(z>=0)
			{
				if(record[temp][z]=='+')
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
				if(record[temp][z]=='+')
				{
					record[temp][z]='-';
				}
				else
				{
					record[temp][z]='+';
				}
				z--;
			}
			numberOfFlips++;
		}
		result[temp]=numberOfFlips;
		temp++;
	}
	temp=0;
	while(temp<t)
	{
		cout<<"case #"<<(temp+1)<<": "<<result[temp]<<endl;
		temp++;
	}
	return 0;
}