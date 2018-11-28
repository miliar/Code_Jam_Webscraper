#include <iostream>
using namespace std;
int main(void)
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<j<<": ";
		for(int i=0;i<s;i++)
			cout<<i+1<<" ";
		cout<<endl;
	}
}