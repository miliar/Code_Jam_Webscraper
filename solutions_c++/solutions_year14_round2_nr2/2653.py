#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, a, b, k, i, j, count;
	cin >> t;
	for (int iter = 1; iter <= t; iter++)
	{
		cin >> a >> b >> k;
		count = 0;
		for (i = 0; i < a; i++)
			for (j = 0; j < b; j++)
			{	
				if ((i&j) < k)
					count++;
			}
		cout << "Case #" << iter << ": " << count << endl;
	}
	return 0;
}