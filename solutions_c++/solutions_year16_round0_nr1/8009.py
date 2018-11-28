#include <bits/stdc++.h>
using namespace std;

bool isComp(int Arr[],int s)
{
	for(int i=0;i<s;i++)
	{
		if(Arr[i]==0)
		return false;
	}
	return true;
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int* Digits= new int[10];
		memset (Digits,0,10);
		int N;
		cin>>N;
		if(N==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		
		else
		{
			int tmp,j;
			for(j=0;!isComp(Digits,10);)
			{
				j++;
				tmp=N*j;	
				while(tmp>0)
				{
					Digits[tmp%10]=1;
					tmp/=10;
				}
			}
			
			cout<<"Case #"<<i<<": "<<N*j<<endl;
		}
	}
}
