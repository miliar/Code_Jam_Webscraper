#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

bool allOne(int arr[], int len)
{
	int flag=1;
	for(int i=0;i<=9;i++)
	{
		if(arr[i]==0)
			flag=0;
	}
	//cout<<flag<<"\n";
	if(flag==1)
		return 1;
	else
		return 0;
}

int main()
{
	long long int T;
	cin>>T;
	long long casse=1;
	unsigned long long int temp_int;
	while(casse<=T)
	{
		int arr[9];
		for(int m=0;m<=9;m++)
		{
			arr[m]=0;
		}
		unsigned long long int N;
		cin>>N;
		if(N==0)
		{
			cout<<"Case #"<<casse<<":"<<" "<<"INSOMNIA"<<"\n";
			casse++;
			continue;
		}
		int flag=0;
		long long int i=0;
		while(flag!=1)
		{
			i++;
			temp_int=i*N;
			string str;
			str=to_string(temp_int);
			long long int k=0;
			while(str[k]!='\0')
			{				
				if(arr[str[k]-'0']==0)
				{
					arr[str[k]-'0']=1;
				}
				if(allOne(arr, 9))
				{
					flag=1;
					break;
				}
				k++;
			}			
		}
		cout<<"Case #"<<casse<<":"<<" "<<temp_int<<"\n";
		casse++;
	}
}
