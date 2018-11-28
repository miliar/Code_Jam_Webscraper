#include <bits/stdc++.h>

using namespace std;

int main()
{
	int testcases;

	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		string a;
		cin >> a;

		string res = (string) "" + a[0];
		// cout << "\t" << res << "\n\t" << a << endl;
		char first = a[0], last = res[res.length() - 1];

		for(int j = 1; j < a.length(); j++)
		{
			if(a[j] >= first)
			{
				res = a[j] + res;
				first = a[j];
			}
			else
			{
				res = res + a[j];
				last = a[j];
			}
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}