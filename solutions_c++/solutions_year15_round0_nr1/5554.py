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

void solve()
{
	int t;
	cin >> t;

	for (int f = 1; f <= t; ++f)
	{
		int n;
		cin >> n;
		string a;
		cin >> a;
		int stay = 0;
		int need = 0;

		for (int i = 0; i < a.size(); ++i)
		{
			if (stay < i)
				need++, stay++;
			stay += (a[i] - '0');
		}
		cout << "Case #" << f << ": " << need << endl;
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(PROBLEM".in", "r", stdin); freopen(PROBLEM".out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	solve();

	return 0;
}
#endif