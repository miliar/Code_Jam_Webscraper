#include<iostream>
using namespace std;
int main()
{
	freopen("output.txt","w",stdout);
	freopen("D-small-attempt0.in","r",stdin);
	int t,l;
	cin>>t;
	l=t;
	while(t--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<l-t<<":"<<" ";
		for(int i=1;i<=k;i++)
		{
			cout<<i<<" ";
		}
		cout<<endl;
	}
	return 0;
}
