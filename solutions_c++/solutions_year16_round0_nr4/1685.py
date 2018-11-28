#include<iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	int Case=1;
	while(t--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<Case<<": ";
		for(int i=1;i<=k;i++)
		cout<<i<<" ";
		cout<<endl;
		Case++;
	}
	return 0;
}
