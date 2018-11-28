#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	
	int k[t];
	int c[t];
	int s[t];
	
	for (int i=0;i<t;i++)
	{
		cin>>k[i]>>c[i]>>s[i];
	}
	
	for (int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<":";
		for (int j=1;j<=s[i];j++)
		{
			cout<<" "<<j;
		}
		cout<<endl;
	}
}
