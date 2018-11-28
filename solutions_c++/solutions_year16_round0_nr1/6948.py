#include <bits/stdc++.h>
using namespace std;
int arr[11];
bool test()
{
	for(int i=0;i<=9;i++)
	{
		if(!arr[i])
			return false;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	int j=0;
	while(j<t)
	{
		long n;
		cin>>n;
		memset(arr,0,sizeof(arr));
		if(n==0)
			cout<<"Case #"<<j+1<<": INSOMNIA"<<endl;
		else
		{
			long i=1;
			while(!test())
			{
				unsigned long long x=n*i;	
				while(x)
				{	
					arr[x%10]=1;
					x=x/10;		
				}
				i++;
			}
			cout<<"Case #"<<j+1<<": "<<n*(--i)<<endl;
		}
		j++;	
	}
}