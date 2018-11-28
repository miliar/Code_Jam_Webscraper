#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cstdint>
using namespace std;

void solve(int test_case)
{
	int n, c;
	cin >> n >> c;
	cout << "Case #" << test_case << ": " << endl;
	for (int64_t i = 0; c > 0 && i < (1ll << (n-2)); ++i)
	{
		vector<int64_t> ans;
		for (int64_t p = 2; p <= 10; ++p)
		{
			for (int64_t j = 2; j <= 100; ++j)
			{
				int64_t pw = 1;
				int64_t d = 0;
				int64_t tmp = (1ll << (n-1)) | (i << 1ll) | 1ll;
				bool is = false;
				while (tmp)
				{
					int64_t cur = tmp & 1;
					tmp >>= 1;
					d = (pw * cur + d) % j;
					pw *= p;
					if (d == 0 && tmp)
					{
						is = true;
					}
				}
				if (d == 0 && is)
				{
					ans.push_back(j);
					break;
				}
			}
		}

		if (ans.size() == 9)
		{
			int64_t tmp = (1ll << (n - 1)) | (i << 1ll) | 1ll;
			string str;
			while (tmp)
			{
				int cur = tmp & 1;
				tmp >>= 1;
				str.push_back(cur + '0');
			}
			std::reverse(str.begin(), str.end());
			cout << str << " ";
			for (int j = 0; j < (int)ans.size(); ++j)
			{
				cout << ans[j] << " ";
			}
			cout << endl;
			--c;
		}
	}
	if (c > 0)
	{
		cout << "error" << endl;
	}
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		solve(i+1);
	}
}