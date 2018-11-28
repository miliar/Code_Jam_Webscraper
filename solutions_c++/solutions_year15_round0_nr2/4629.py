#if 1
#include <iostream>
#include <cstdio>
#include <numeric>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <locale>

using namespace std;
#define PROBLEM "problem"
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> pii;
#define X first 
#define Y second 

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1LL * INF * INF;
const LL mod = INF + 7;


map<vector<int>, int> res;

int rec(vector<int> a)
{
	sort(a.begin(), a.end());

	if (res.count(a))
		return res[a];

	int pos = max_element(a.begin(), a.end()) - a.begin();
	int ans = a[pos];

	if (ans < 2)
	{
		res[a] = ans;
		return ans;
	}

	for (int i = 1; i < a[pos]; ++i)
	{
		a.push_back(i);
		a[pos] -= i;
		ans = min(ans, rec(a) + 1);
		a[pos] += a.back();
		a.pop_back();
	}

	res[a] = ans;
	return ans;
}

void solve()
{
	int t;
	cin >> t;

	for (int f = 1; f <= t; ++f)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		cout << "Case #" << f << ": " << rec(a) << endl;
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen(PROBLEM".in", "r", stdin); freopen(PROBLEM".out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	solve();

	return 0;
}
#endif