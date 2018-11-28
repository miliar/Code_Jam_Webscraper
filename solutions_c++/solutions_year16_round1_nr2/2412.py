#include <iostream>
using namespace std;

int main() {
	int t,n,e;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>n;
		int a[2501] = {0};
		for(int j = 0; j < 2*n - 1; j++)
		{
			for(int k = 0; k < n; k++)
			{
				cin>>e;
				a[e]++;
			}
		}
		cout<<"Case #"<<i<<": ";
		for(int l = 1; l <=2500; l++)
		{
			if(a[l] & 1)
				cout<<l<<" ";
		}
		cout<<endl;
	}
	return 0;
}