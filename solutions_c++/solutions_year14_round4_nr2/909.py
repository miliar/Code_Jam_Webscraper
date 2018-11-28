#if 1
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <numeric>
#include <cstring>
#include <ctime>


using namespace std;
#define mp make_pair
#define X first
#define Y second
#define pb push_back

typedef pair<int, int> pii ;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;

const LL inf = 1e9;
const LD eps = 1e-9;

int dist(vector <int> &a, vector <int> &b)
{
	map<int, int> pos;
	for (int i = 0; i < a.size(); i++)
	{
		pos[a[i]] = i;
	}

	int cnt = 0;
	for (int i = 0; i < a.size(); i++)
	{
		for (int k = i + 1; k < a.size(); k++)
		{
			if (pos[b[i]] > pos[b[k]])
				cnt++;
		}
	}
	return cnt;
}
int main()        
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		int n;
		scanf("%d", &n);
		vector <int> a(n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		vector <int> b = a;
		sort(b.begin(), b.end());
		int ans = inf;
		do
		{
			int maxPos = max_element(b.begin(), b.end()) - b.begin();
			bool fl = 1;
			for (int i = 0; i < maxPos - 1; i++)
			{
				if (b[i] > b[i + 1])
				{
					fl = 0;
					break;
				}
			}
			for (int i = maxPos; i < n - 1; i++)
			{
				if (b[i] < b[i + 1])
				{
					fl = 0;
					break;
				}
			}
			if (fl)
				ans = min(ans, dist(b, a));
		}
		while (next_permutation(b.begin(), b.end()));
		printf("Case #%d: %d\n", q + 1, ans);
	}
    return 0;
}
#endif