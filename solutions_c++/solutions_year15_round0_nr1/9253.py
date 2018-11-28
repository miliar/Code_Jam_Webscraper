#include<iostream>
using namespace std;
#include<stdlib.h>
int main()
{
	freopen("in.cpp", "r", stdin);
    freopen("out.cpp", "w", stdout);
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int smax;
		cin>>smax;
		char arr[smax+5];
		int count=0;
		int prev=0;
		cin>>arr;
		prev=arr[0]-'0';
		for(int i=1;i<=smax;i++)
		{
			
			if( prev < i && (arr[i]-'0')!=0)
			{
				count+=(i-prev);
				prev+=(i-prev);
				prev+=arr[i]-'0';
			}
			else
			 prev+=arr[i]-'0';
		}
		cout<<"Case #"<<k+1<<": "<<count<<"\n";
	}
	return 0;
}
