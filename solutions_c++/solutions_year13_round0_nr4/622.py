#include <iostream>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

int key_cnt[200];

struct Chest
{
	int lock_type;
	vector<int> keys;
};

int memo[1048576];

vector<Chest> chest;
vector<int> answer;

bool solve(int open_map)
{
	if (memo[open_map] != 0) return memo[open_map] == 1;
	const int N = chest.size();
	int ans = -1;

	for (int j = 0, m = 1; j < N; ++j, m *= 2)
	{
		int kt = chest[j].lock_type;
		if ((open_map & m) == 0 && key_cnt[kt] > 0)
		{
			key_cnt[kt]--;
			for (int k = 0; k < chest[j].keys.size(); ++k)
			{
				key_cnt[chest[j].keys[k]]++;
			}
			bool solvable = solve(open_map | m);

			for (int k = 0; k < chest[j].keys.size(); ++k)
			{
				key_cnt[chest[j].keys[k]]--;
			}
			key_cnt[kt]++;

			if (solvable)
			{
				answer.push_back(j);
				ans = 1;
				break;
			}
		}
	}

	memo[open_map] = ans;
	return ans == 1;
}

void reset(int N)
{
	answer.clear();
	chest.clear();
	memset(key_cnt, 0, sizeof(key_cnt));

	int m = 1;
	while (N--) m *= 2;

	memset(memo, 0, m*sizeof(int));
	memo[m-1] = 1;
}

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; ++casenum)
	{
		int K, N;
		cin >> K >> N;

		reset(N);

		while (K--)
		{
			int k;
			cin >> k;
			--k;
			key_cnt[k]++;
		}

		while (N--)
		{
			int Ti, Ki;
			cin >> Ti >> Ki;
			chest.push_back(Chest());

			Chest &c = chest.back();

			c.lock_type = Ti - 1;
			while (Ki--)
			{
				int k;
				cin >> k;
				--k;
				c.keys.push_back(k);
			}
		}

		cout << "Case #" << casenum << ": ";
		bool solvable = solve(0);
		if (solvable)
		{
			assert(answer.size() == chest.size());
			for (int j = answer.size()-1; j >= 0; --j)
			{
				cout << answer[j]+1 << ' ';
			}
		}
		else
		{
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}

	return 0;
}
