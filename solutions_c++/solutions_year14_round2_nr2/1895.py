#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	int count = 0;
	while (T--)
	{
		if (count != 0)
			cout << endl;
		count++;
		cout << "Case #" << count << ": ";
		int a, b, k;
		cin >> a >> b >> k;
		int result = 0;
		for (int i = 0; i < a; i++)
		{
			for (int j = 0; j < b; j++)
			{
				int r = i&j;
				if (r < k)
					result++;
			}
		}

		cout << result;


	}
	return 0;
}