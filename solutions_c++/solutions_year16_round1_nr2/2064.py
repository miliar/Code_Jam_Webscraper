#include<iostream>
using namespace std;
int main()
{
	int t, n;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		int k;
		cout << "Case #" << i << ": ";
		cin >> n;
		int a[2501]={0};
		int l=(2*n*n-n);
		for(int j=0;j<l;j++)
		{
			cin >> k;
			a[k]++;
		}
		for(int j=1;j<2501;j++)
		{
			if(a[j]%2!=0)
				cout << j << " ";
		}
		cout << endl;
	}
}

