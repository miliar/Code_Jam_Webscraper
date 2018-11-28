#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		unsigned long long int N;
		cin >> N;
		if (N == 0)
		{
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
		else
		{
			bool vis[10];
			for (int j = 0; j < 10; ++j)
			{
				vis[j] = false;
			}
			int count_vis = 0;
			bool find_ans = false;
			unsigned long long int cur = 0;
			while(!find_ans)
			{
				cur += N;
				unsigned long long int tmp = cur;
				while(tmp > 0)
				{
					int digit = tmp % 10;
					if (!vis[digit])
					{
						++count_vis;
					}
					vis[digit] = true;
					tmp /= 10;
				}
				if (count_vis == 10)
				{
					cout << "Case #" << i+1 << ": " << cur << endl;
					find_ans = true;
				}
			}
		}
	}
	return 0;
}

