#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main()
{
	//freopen("C:/Users/wanyunpeng/Desktop/in.in", "r", stdin);
	//freopen("C:/Users/wanyunpeng/Desktop/out.txt", "w", stdout);
	//freopen("C:/Users/wanyunpeng/Desktop/large.in", "r", stdin);
	//freopen("C:/Users/wanyunpeng/Desktop/large-out.txt", "w", stdout);
	int cas;
	cin >> cas;
	int i = 1;
	while (cas--)
	{
		int n;
		cin >> n;
		unordered_map<int, int> mm;
		for (int i = 0; i < 2 * n - 1; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				int num;
				cin >> num;
				mm[num]++;
			}
		}
		vector<int> res;
		for (auto tmp : mm)
		{
			if (tmp.second % 2 != 0)
				res.push_back(tmp.first);
		}
		sort(res.begin(), res.end());
		cout << "Case #" << i++ << ":";
		for (auto r : res)
		{
			cout << " " << r;
		}
		cout << endl;
	}
	return 0;
}