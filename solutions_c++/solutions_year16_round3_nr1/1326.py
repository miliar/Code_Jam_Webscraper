#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <queue>
using namespace std;
int n, t, tt, cnt[30], sum;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++)
	{
		printf("Case #%d:", tt);
		sum = 0;
		priority_queue<pair<int, int> > q;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", cnt + i), q.push({cnt[i], i}), sum+=cnt[i];
		while (sum!=3 && sum)
		{
			sum -= 2;
			pair<int, int> a, b;
			a = q.top();
			q.pop();
			a.first--;
			q.push(a);
			b = q.top();
			q.pop();
			b.first--;
			q.push(b);
			printf(" %c%c", a.second + 'A', b.second + 'A');
		}
		if (sum == 3)
		{
			pair<int, int> a, b;
			a = q.top(), q.pop();
			a.first--;
			q.push(a);
			printf(" %c", a.second + 'A');
			a = q.top(), q.pop();
			a.first--;
			q.push(a), b = q.top();
			q.pop();
			b.first--;
			q.push(b);
			printf(" %c%c", a.second + 'A', b.second + 'A');
		}
		printf("\n");
	}
	return 0;
}