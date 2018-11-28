#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		int k, c, s;
		cin >> k >> c >> s; 
		cout << "Case #" << (q + 1) << ": ";
		for (int i = 1; i <= k; i++)
		{
			cout << i;
			if (i < k)
				cout << " ";
		}
		cout << "\n";
	}
	return 0;
}