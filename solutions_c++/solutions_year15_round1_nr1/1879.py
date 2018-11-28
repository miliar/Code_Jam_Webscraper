#include <iostream>

#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;

	cin >> T;

	for(int tc = 0; tc < T; ++tc)
	{
		int n, first = 0, second = 0, mx = 0;

		cin >> n;

		vector<int> data(n);

		for(int i = 0; i < n; ++i)
		{
			cin >> data[i];
		}

		for(int i = 1; i < n; ++i)
		{
			if(data[i] < data[i - 1])
			{
				first += data[i - 1] - data[i];
				mx = max(mx, data[i - 1] - data[i]);
			}
		}
		
		for(int i = 0; i < n - 1; ++i)
		{
			second += min(mx, data[i]);
		}

		cout << "Case #" << tc + 1 << ": " << first << ' ' << second << endl;
	}

	return 0;
}