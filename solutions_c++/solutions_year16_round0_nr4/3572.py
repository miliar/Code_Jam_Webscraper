#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<(i+1)<<": ";
		for(int j=1;j<=k;j++)
		{
			cout<<j<<" ";
		}
		cout<<endl;
	}
	return 0;
}