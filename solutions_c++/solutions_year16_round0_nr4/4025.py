#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		int K,C,S;
		cin>>K>>C>>S;
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=K-1;j++)cout<<j<<" ";
		 cout<<K<<"\n";
	}
	return 0;
}