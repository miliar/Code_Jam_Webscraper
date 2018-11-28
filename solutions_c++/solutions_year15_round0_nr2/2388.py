#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int n, cnt[1005] = { };
		cin >> n;
		while(n--)
		{
			int x;
			cin >> x;
			cnt[x]++;
		}

		int ans = 1000000;
		for(int i = 1000; i > 0; i--)
		{
			int cur = 0;
			for(int j = i + 1; j <= 1000; j++)
			{
				cur += cnt[j]*(j/i + (j%i != 0) - 1);
			}
			ans = min(cur + i, ans);
		}

		cout << "Case #" << t << ": " << ans << '\n';
	}
}