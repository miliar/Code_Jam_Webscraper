#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::vector<int> vi;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

const int size = 2000;
const int infty = 10000;
std::vector<int> edge[size];
std::vector<int> weak[size];
int a[size], b[size];
int deg[size];
int ans[size];

vi calc_a(vi ar)
{
	int n = (int) ar.size();
	vi ans;
	for(int i = 0; i < n; i++)
	{
		int curans = 1;
		for(int j = 0; j < i; j++)
			if (ar[j] < ar[i])
				curans = std::max(curans, ans[j] + 1);
		ans.push_back(curans);
	}
	return ans;
}

vi calc_b(vi ar)
{
	int n = (int) ar.size();
	std::reverse(ar.begin(), ar.end());
	vi ans;
	for(int i = 0; i < n; i++)
	{
		int curans = 1;
		for(int j = 0; j < i; j++)
			if (ar[j] < ar[i])
				curans = std::max(curans, ans[j] + 1);
		ans.push_back(curans);
	}
	std::reverse(ans.begin(), ans.end());
	return ans;
}



void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		edge[i].clear();
		weak[i].clear();
	}
	for(int i = 0; i < n; i++)
		scanf("%d\n", &a[i]);
	for(int i = 0; i < n; i++)
		scanf("%d\n", &b[i]);
	for(int i = 0; i < n; i++)
		for(int j = i+1; j < n; j++)
		{
			if (a[i] >= a[j] || b[i] - b[j] >= j - i)
			{
				edge[j].push_back(i);
				deg[i]++;
			}
			if (b[i] <= b[j] || a[j] - a[i] >= j - i)
			{
				edge[i].push_back(j);
				deg[j]++;
			}
			if (b[i] == b[j] + 1)
			{
				weak[j].push_back(i);
				if (deg[i] < infty)
					deg[i] += infty;
			}
		}
	std::set<pii> heap;
	for(int i = 0; i < n; i++)
		heap.insert(pii(deg[i], i));
	for(int i = 0; i < n; i++)
	{
		pii cur = *heap.begin();
		if (cur.first != 0)
			throw 42;
		int u = cur.second;
		ans[u] = i;
		heap.erase(heap.begin());
		for(int j = 0; j < (int) edge[u].size(); j++)
		{
			int v = edge[u][j];
			heap.erase(heap.find(pii(deg[v], v)));
			deg[v]--;
			heap.insert(pii(deg[v], v));
		}
		for(int j = 0; j < (int) weak[u].size(); j++)
		{
			int v = weak[u][j];
			if (deg[v] >= infty)
			{
				heap.erase(heap.find(pii(deg[v], v)));
				deg[v]-=infty;
				heap.insert(pii(deg[v], v));
			}
		}
	}

	vi zzz;
	for(int i = 0; i < n; i++)
		zzz.push_back(ans[i]);
	vi aa = calc_a(zzz);
	vi bb = calc_b(zzz);
	for(int i = 0; i < n; i++)
		if (aa[i] != a[i] || bb[i] != b[i])
		{
			printf("a:\n");
			printf("My      : ");
			for(int j = 0; j < n; j++)
				printf("%d ", aa[j]);
			printf("\n");
			printf("Expected: ");
			for(int j = 0; j < n; j++)
				printf("%d ", a[j]);
			printf("\n");
			printf("b:\n");
			printf("My      : ");
			for(int j = 0; j < n; j++)
				printf("%d ", bb[j]);
			printf("\n");
			printf("Expected: ");
			for(int j = 0; j < n; j++)
				printf("%d ", b[j]);
			printf("\n");
			//printf("Fail\n");
			exit(0);
		}
	
	for(int i = 0; i < n; i++)
		printf("%d ", ans[i] + 1);
	printf("\n");
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
