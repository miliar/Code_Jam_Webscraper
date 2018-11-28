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
		int k;

		cin >> k;

		string data;

		cin >> data;

		int count = 0;

		int ans = 0;

		for(int i = 0; i <= k; ++i)
		{
			if(data[i] - '0')
			{
				if(i <= count)
				{
					count += data[i] - '0';
				}
				else
				{
					ans += i - count;
					count += data[i] - '0' + i - count;
				}
			}
		}
		cout << "Case #" << tc + 1 << ": " << ans << endl;
	}

	return 0;
}