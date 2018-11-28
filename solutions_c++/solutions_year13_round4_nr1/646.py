#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <stack>
using namespace std;

const int maxn = 1010, maxs = 2010;
const int key = 1000002013;

int dat[maxn][3], n, m;

int add(int x, int y) { return ((long long)x + y) % key; }
int mul(int x, int y) { return ((long long)x * y) % key; }
int subs(int x, int y) { return (((long long)x - y) % key + key) % key; }
int sqr(int x, int y) { return mul(x, x); }
int div2(int x) { return (x & 1) ? ((long long)x + key) / 2 % key : x / 2 % key; }
int sums(int n) { return div2(mul(n, n - 1)); }

int points[maxs], pcnt;
void renum()
{
	pcnt = 0;
	points[pcnt++] = 1;
	points[pcnt++] = n;
	for (int i = 0; i < n; i++)
	{
		points[pcnt++] = dat[i][0];
		points[pcnt++] = dat[i][1];
	}
	
	sort(points, points + pcnt);
	pcnt = unique(points, points + pcnt) - points;

	for (int i = 0; i < n; i++)
	{
		dat[i][0] = lower_bound(points, points + pcnt, dat[i][0]) - points;
		dat[i][1] = lower_bound(points, points + pcnt, dat[i][1]) - points;
	}
}

long long flow[maxs];
void getflow()
{
	for (int i = 0; i < pcnt; i++) flow[i] = 0;
	for (int i = 0; i < n; i++)
	{
		flow[dat[i][0]] += dat[i][2];
		flow[dat[i][1]] -= dat[i][2];
	}
	for (int i = 1; i < pcnt; i++) flow[i] += flow[i - 1];
}

int calccont()
{
	int ans = 0;
	stack<pair<int, long long> > S;
	for (int i = 0; i < pcnt; i++)
	{
		int start = points[i];
		while (!S.empty() && S.top().second >= flow[i])
		{
			pair<int, long long> tmp = S.top();
			S.pop();
			long long fact = tmp.second - flow[i];
			if (!S.empty()) fact = min(fact, tmp.second - S.top().second);
			ans = add(ans, mul(sums(points[i] - tmp.first), fact % key));
			start = tmp.first;
		}
		
		S.push(make_pair(start, flow[i]));
	}
	
	return ans;
}

void init()
{
	scanf("%d%d", &m, &n);
	for (int i = 0; i < n; i++) scanf("%d%d%d", &dat[i][0], &dat[i][1], &dat[i][2]);
}

void work()
{
	int orig = 0;
	for (int i = 0; i < n; i++)
		orig = add(orig, mul(sums(dat[i][1] - dat[i][0]), dat[i][2]));
	
	renum();
	getflow();
	int ans = calccont();
	
	printf("%d\n", subs(ans, orig));
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		init();
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
