#include<iostream>
using namespace std;

int main()
{
	freopen("ccc.in", "r", stdin);
	freopen("output3.out", "w", stdout);
	int T;
	cin>>T;
	for (int i=1; i<=T; i++)
	{
		int K,S,C;
		cin>>K>>S>>C;
		cout<<"Case #"<<i<<": ";
		for (int i=1; i<=K; i++)
		{
			cout<<i<<" ";
		}
		cout<<endl;
	}
	return 0;
}
