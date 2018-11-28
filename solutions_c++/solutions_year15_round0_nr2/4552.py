//g++ -std=c++0x your_file.cpp -o your_program
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define fname "B-small-attempt7"
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

multiset <int> q;

int a[111];

int n;

int cur, ans;

void rec()
{
	ans = min(ans, cur + *q.rbegin());
	if (ans - cur <= 2)
		return ;
	int val = *q.rbegin();
	set <int> :: iterator it = q.end();
	it--;
	q.erase(it);
	for (int j = 1; j <= val / 2; j++)
	{
		q.insert(j);
		q.insert(val - j);
		cur++;
		rec();
		cur--;
		q.erase(q.find(j));
		q.erase(q.find(val - j));
	}
	q.insert(val);
}

int main()
{
	freopen (fname".in", "r", stdin);
	freopen (fname".out", "w", stdout);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		scanf("%d", &n);
		int x;
		q.clear();
		ans = 0;
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &x);
			q.insert(x);
			ans = max(ans, x);
		}
		cur = 0;
		rec();
		printf("%d\n", ans);
	}
	return 0;
}
