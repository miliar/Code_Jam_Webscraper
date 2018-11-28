#include<bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int Case=1;
	while(test--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<Case<<": ";
		for(int i=0;i<k-1;++i)
		{
			cout<<(i+1)<<" ";
		}
		cout<<k<<endl;
		Case++;
	}
	return 0;
}
