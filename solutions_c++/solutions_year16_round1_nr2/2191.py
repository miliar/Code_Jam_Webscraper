#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n;
		cin>>n;
		int sz = 2*n-1;
		int input[sz][n];
		vector<int> ans;
		int count[2501] = {};
		for(int i=0;i<sz;i++)
			for(int j=0;j<n;j++)
			{
				cin>>input[i][j];
				count[input[i][j]]++;
			}
		cout<<"Case #"<<t<<": ";
		for(int i=1;i<=2500;i++)
			if(count[i]%2)
				cout<<i<<" ";
		cout<<"\n";		
		
	}
	return 0;
}
