#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<(j+1)<<": ";
		for(int i=1;i<=k;i++)
		{
			cout<<i<<" ";
		}
		cout<<"\n";
	}
	return 0;
}