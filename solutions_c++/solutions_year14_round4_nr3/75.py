#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
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

const int size = 1500;
int n, m, b;

class rect
{
public:
	int x1, y1, x2, y2;
	rect(){}
	rect(int x1, int y1, int x2, int y2) : x1(x1), y1(y1), x2(x2), y2(y2){};
	void read()
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
	}
	void inc()
	{
		x1--; y1--;
		x2++; y2++;
	}
	int dist(const rect &other)
	{
		return std::max(
				std::max(0, std::max(x1, other.x1) - std::min(x2, other.x2) - 1),
				std::max(0, std::max(y1, other.y1) - std::min(y2, other.y2) - 1)
				);
	}
	bool touch(const rect &other)
	{
		return dist(other) == 0;
	}
} ar[size];

class set
{
public:
	int p[size];
	int w[size];
	void init()
	{
		for(int i = 0; i < size; i++)
		{
			p[i] = i;
			w[i] = 1;
		}
	}
	int find(int x)
	{
		if (x != p[x])
			p[x] = find(p[x]);
		return p[x];
	}
	void merge(int a, int b)
	{
		a = find(a); b = find(b);
		if (a == b)
			return;
		if (w[a] > w[b])
			p[b] = p[a];
		else
			p[a] = p[b];
		if (w[a] == w[b])
			w[b]++;
	}
} adj;

int dist[size];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	scanf("%d%d%d", &n, &m, &b);
	for(int i = 0; i < b; i++)
		ar[i].read();
	ar[b] = rect(-1, 0, -1, m-1);
	ar[b+1] = rect(n, 0, n, m-1);
	b += 2;
	for(int i = 0; i < b; i++)
		dist[i] = (int) 1e9;
	dist[b-2] = 0;
	std::set<pii> heap;
	for(int i = 0; i < b; i++)
		heap.insert(pii(dist[i], i));
	while(!heap.empty())
	{
		int cur = heap.begin()->second;
		heap.erase(heap.begin());
		for(int i = 0; i < b; i++)
			if (dist[i] > dist[cur] + ar[cur].dist(ar[i]))
			{
				heap.erase(heap.find(pii(dist[i], i)));
				dist[i] = dist[cur] + ar[cur].dist(ar[i]);
				heap.insert(pii(dist[i], i));
			}
	}
	printf("%d\n", dist[b-1]);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
