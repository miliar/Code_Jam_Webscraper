#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int n[t],height;
		int ar[t][2501];
	for (int i = 0; i < t; i++)
	{
		cin>>n[i];
		for (int j = 0; j < 2*n[i]*n[i]-n[i]; j++)
		{
			cin>>height;
			ar[i][height]++;
		}
	}

	for (int i = 0; i < t; i++)
	{
		// cin>>n;
		// int ar[2501]={0};
		
		int ans[n[i]],poi=0;
		for (int j = 0; poi < n[i]; j++)
		{
			// cout<<ar[j]<<' ';
			if (ar[i][j]%2)
			{
				ans[poi]=j;
				poi++;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for (int j = 0; j < n[i]; j++)
		{
			cout<<ans[j]<<' ';
		}
		cout<<endl;
	}
	return 0;
}