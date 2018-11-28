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
		int n;

		cin >> n;

		multiset<int, greater<int>> data, data_tmp;

		for(int i = 0; i < n; ++i)
		{
			int tmp;
			cin >> tmp;
			data.insert(tmp);
		}

		int ans = *data.begin();

		int left = 1, right = *data.begin();

		for(int x = right - 1; x >= left; --x)
		{
			int count = 0;
			data_tmp.clear();
			for(multiset<int, greater<int>>::iterator it = data.begin(); it != data.end(); ++it)
			{
				int cur = *it;
				while(cur > x)
				{
					data_tmp.insert(x);
					cur -= x;
					++count;
				}

				data_tmp.insert(cur);
			}

			ans = min(ans, x + count);
		}

		//while(*data.begin() > 1)
		//{
		//	++count;

		//	int tmp = *data.begin();

		//	data.erase(data.begin());

		//	data.insert(tmp / 2);

		//	if(tmp & 1)
		//		data.insert(tmp / 2 + 1);
		//	else
		//		data.insert(tmp / 2);

		//	ans = min(ans, *data.begin() + count);
		//}

		cout << "Case #" << tc + 1 << ": " << ans << endl;
	}

	return 0;
}