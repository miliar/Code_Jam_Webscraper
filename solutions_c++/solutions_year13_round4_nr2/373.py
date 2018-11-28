/*
 * program: google code jam 2013 round 2. b
 * writer: 67h2gak
 * date: 2013.6.1
*/
#include <cmath>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long LL;

int n; LL p, ans0, ans1;

void init()
{
	scanf("%d%lld", &n, &p);
}

LL solve0(int n, LL x, LL p)//anyway
{
	if (p <= 0) return 0;
	if (x <= 1) return 1;
	LL s = (x - 2) / 2;
	if (solve0(n - 1, s + 1, p - (1LL << (n - 1)))) return 1;
	return 0;
}

LL solve1(int n, LL x, LL p)//someway
{
	//printf("%d, %lld, %lld\n", n, x, p);
	if (p <= 0) return 0;
	if (x <= p) return 1;
	if (x == (1LL << n) && p < (1LL << n)) return 0;
	LL s = x / 2;
	if (s + 1 <= (1LL << (n-1)) &&  solve1(n - 1, s + 1, p)) return 1;
	return 0;
}

void work()
{
	LL l = 1, r = 1LL << n;
	while (l < r){
		LL mid = (l + r + 1) >> 1;
		if (solve0(n, mid, p)) l = mid;
			else r = mid - 1;
	}
	ans0 = l;
	
	l = 1, r = 1LL << n;
	while (l < r){
		LL mid = (l + r + 1) >> 1;
		//puts("");
		if (solve1(n, mid, p)) l = mid;
			else r = mid - 1;
	}
	ans1 = l;
}

void print()
{
	printf("%lld %lld\n", ans0 - 1, ans1 - 1);
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t ++){
		init();
		work();
		printf("Case #%d: ", t);
		print();
	}
	return 0;
}
