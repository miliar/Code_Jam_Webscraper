#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <climits>
using namespace std;


#if 1
int main()
{
	//A-large
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T = 0;
	cin >> T;
	for (int nCase = 1; nCase <= T; ++nCase)
	{
		int N = 0;
		cin >> N;
		vector<int> mush(N, 0);
		for (int i = 0; i < N; ++i)
		{
			cin >> mush[i];
		}

		int ans1 = 0;
		for (int i = 1; i < N; ++i)
		{
			if (mush[i-1] > mush[i])
			{
				ans1 += mush[i-1] - mush[i];
			}
		}

		
		int maxdiff = 0;
		for (int i = 1; i < N; ++i)
		{
			if (mush[i-1] > mush[i])
			{
				maxdiff = max(maxdiff, mush[i-1] - mush[i]);
			}
		}

		double speed = maxdiff / 10.0;
		int ans2 = INT_MAX;
		//double speed = (mush[N-2] - mush[N-1]) / 10.0;
		int sum = 0;
		for (int i = 0; i < N - 1; ++i)
		{
			if (speed * 10.0 >= mush[i])
			{
				sum += mush[i];
			}
			else
			{
				sum += speed * 10.0;
			}
		}

		ans2 = sum;


		cout << "Case #" << nCase << ": " << ans1 << " " << ans2 << endl;

	}
	return 0;
}
#endif //0