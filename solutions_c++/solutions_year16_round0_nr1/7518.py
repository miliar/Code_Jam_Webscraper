#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <cstring>
#include <tuple>
#include <cassert>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		int i;
		cin >> i;
		bool seen[10] = { };
		int cnt = 0;
		if(i == 0) cout << "INSOMNIA\n";
		else
		{
			for(long long j = i; true; j += i)
			{
				long long k = j;
				while(k > 0)
				{
					if(!seen[k % 10])
					{
						seen[k % 10] = true;
						cnt++;
					}
					k /= 10;
				}
				if(cnt == 10)
				{
					cout << j << '\n';
					break;
				}
			}

		}
	}

	return 0;
}
