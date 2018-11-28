#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <assert.h>
#include <stack>
const int N = 6005;
using namespace std;

typedef long long lld;
const lld P = 1000002013;
const lld inv2 = (1000002013LL + 1) / 2;

struct People {
	int a, b, c;
} people[N];

struct Item {
	lld x;
	lld cnt;
};

stack<Item> S;
lld v[N];
lld deserved, reality;
int T, n, m;
int X[N];
int cX;

lld cost(lld s)
{
	lld a = n;
	lld b = (n + 1 - s);
	lld h = s;
	return ((a + b) * s) % P * inv2 % P;
}

int find(int v)
{
	return lower_bound(X, X + cX, v) - X;
}

void gao(int left, int right)
{
	if (left >= right) return;
	if (v[left] == 0) {
		gao(left + 1, right);
		return;
	}
	if (v[right] == 0) {
		gao(left, right - 1);
		return;
	}
	lld c = 0;
	for (int i = left; i <= right; ++i) {
		c += v[i];
		if (c == 0) {
			// left and i
			int p = left, q = i;
			lld delta = min(v[p], -v[q]);
			v[p] -= delta;
			v[q] += delta;
			int orip = (X[p] + 1) / 2;
			int oriq = (X[q] + 1) / 2;
			lld curcost = cost(oriq - orip) * delta % P;
			reality = (reality + curcost) % P;
			gao(left, i);
			gao(i + 1, right);
			break;
		}
	}
}

void work()
{
	cX = 0;
	scanf("%d%d", &n, &m);
	memset(v, 0, sizeof(v));
	deserved = reality = 0;
	for (int i = 1; i <= m; ++i) {
		scanf("%d%d%d", &people[i].a, &people[i].b, &people[i].c);
		X[cX++] = people[i].a * 2 - 1;
		X[cX++] = people[i].b * 2;
		deserved = (deserved + cost(people[i].b - people[i].a) * people[i].c) % P;
	}
	sort(X, X + cX);
	for (int i = 1; i <= m; ++i) {
		int t = find(people[i].a * 2 - 1);
		v[t] += people[i].c;
		int t2 = find(people[i].b * 2);
		v[t2] -= people[i].c;
		assert(t < t2);
	}
	// gao(0, cX - 1);
	while (!S.empty()) S.pop();
	for (int i = 0; i < cX; ++i) if (v[i] != 0) 
		if (v[i] > 0) {
			Item item;
			item.cnt = v[i];
			item.x = X[i];
			S.push(item);
		} else {
			while (v[i] < 0) {
				lld delta = min(-v[i], S.top().cnt);
				S.top().cnt -= delta;
				v[i] += delta;
				int p = (S.top().x + 1) / 2;
				int q = (X[i] + 1) / 2;
				reality = (reality + cost(q - p) * delta) % P;
				if (S.top().cnt == 0) S.pop();
			}
		}
	lld answer = (deserved - reality) % P;
	answer += (answer < 0) * P;
	static int ttt = 0;
	printf("Case #%d: %lld\n", ++ttt, answer);
}

int R()
{
	return rand() * 32768 + rand();
}
void mkdata()
{
	freopen("A-small-at.in", "w", stdout);
	printf("20\n");
	for (int t = 1; t <= 20; ++t) {
		printf("1000000000 1000\n");
		for (int j = 0; j < 1000; ++j) {
			int a = R() % 1000000000 + 1;
			int b = R() % 1000000000 + 1;
			if (a > b) {
				int t = a; a = b; b = t;
			}
			int c = R() % 1000000000 + 1;
			printf("%d %d %d\n", a, b, c);
		}
	}
	exit(0);
}

int main()
{
	//mkdata();
	assert(inv2 * 2 % P == 1);
	freopen("A-large.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	scanf("%d", &T);
	while (T--) work();
}