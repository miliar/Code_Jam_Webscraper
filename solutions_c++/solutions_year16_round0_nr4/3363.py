#include<iostream>
using namespace std;
int main()
{
	int t,s,c,k;
	cin>>t;
	for(int i=1;i<t+1;i++)
	{
		cin>>s>>c>>k;
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=k;j++)
		{
			cout<<j;
			if(j!=k)
			cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}
