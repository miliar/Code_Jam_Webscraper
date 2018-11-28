#include <iostream>
#include <string>
#include <cstring>
#include <cctype>
#include <limits>
#include <vector>
#include <unordered_set>
#include <memory>
#include <algorithm>
#define maxM 2000
#define maxN 2000

using namespace std;

int N, M;
string S[maxN];
int side[maxN];
unordered_set<string> tries[maxM];
int ans, anscnt;

void dfs(int K)
{
	if (K == N)
	{
		for (int i = 0; i < M; i++)
			tries[i].clear();
		for (int i = 0; i < N; i++)
		{
			tries[side[i]].insert("");
			for (int j = 0; j < S[i].length(); j++)
				tries[side[i]].insert(S[i].substr(0, j + 1));
		}
		int cur = 0;
		for (int i = 0; i < M; i++)
			cur += tries[i].size();
		if (cur > ans)
		{
			ans = cur;
			anscnt = 1;
		}
		else if (cur == ans)
			anscnt++;
	}
	else
	{
		for (int i = 0; i < M; i++)
		{
			side[K] = i;
			dfs(K + 1);
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			cin >> S[i];
		ans = 0;
		anscnt = 0;
		dfs(0);
		cout << "Case #" << z << ": " << ans << " " << anscnt << endl;
	}
	return 0;
}
