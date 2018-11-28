#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

int Solution()
{
	int n, m;
	cin >> n >> m;
	vector<vi> v(n, vi(m));
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			cin >> v[i][j];

	vector<int> rowH(n), colH(m);

	for(int i = 0; i < n; ++i)
	{
		int maxH = 0;
		for(int j = 0; j < m; ++j)
			if(v[i][j] > maxH)
				maxH = v[i][j];
		rowH[i] = maxH;
	}

	for(int j = 0; j < m; ++j)
	{
		int maxH = 0;
		for(int i = 0; i < n; ++i)
			if(v[i][j] > maxH)
				maxH = v[i][j];
		colH[j] = maxH;
	}

	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			if(min(rowH[i], colH[j]) != v[i][j])
			{
				cout << "NO";
				return 0;
			}

	cout << "YES";

	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
