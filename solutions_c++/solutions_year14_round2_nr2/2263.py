#include<iostream>
using namespace std;
int main()
{
	int p,t,a,b,k;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int ans = 0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j) < k)
				{
					ans++;
				}
			}
		}
		cout<<"Case #"<<p<<": "<< ans <<endl;
	}
	return 0;
}
