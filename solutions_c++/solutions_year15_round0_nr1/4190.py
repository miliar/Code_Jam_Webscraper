#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int TC;
	cin >> TC;

	for (int cases = 1; cases <= TC; cases++)
	{
		int N;
		string S;

		cin >> N >> S;

		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= N; i++)
		{
			if(S[i] == '0') 
				continue;

			if(sum < i)
			{
				ans += (i - sum);
				sum = i;
			}

			sum += (S[i]-'0');
		}

		cout << "Case #" << cases << ": ";
		cout << ans << "\n";
	}
	
	return 0;
}