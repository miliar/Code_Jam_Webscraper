#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

int word, k, full;
string s, keys;
int mx;
double ex;
map<char, int> keyCnt;

void brute(string t, double prob)
{
	if (t.size() == full)
	{
		int cnt = 0;
		for (int i = 0; i + word - 1 < full; i++)
			if (s == t.substr(i, word))
				cnt++;
		mx = max(cnt, mx);
		ex += cnt * prob;
		return;
	}

	for (auto kk : keyCnt)
	{
		brute(t + kk.first, prob * (1.0 * kk.second / k));
	}
}

void solve()
{
	cin >> k >> word >> full;
	cin >> keys >> s;
	
	mx = 0;
	ex = 0;
	keyCnt.clear();

	for (int i = 0; i < k; i++)
		keyCnt[keys[i]]++;

	brute("", 1);
	printf("%.10lf", mx - ex);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
}