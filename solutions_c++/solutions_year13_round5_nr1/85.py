#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int MAX_N = 100 + 10;
const LL INF = 1000000000000LL;

double ret;
LL N, B, M;
LL a[MAX_N];

int getSum(LL x)
{
	LL sum = 0;
	for(int i = 0; i < 37; ++ i) {
		if (a[i] < x)
			sum += x - a[i];
	}
	return sum <= B;
}

LL calc()
{
	LL l = 0, r = INF + 1, mid;
	for( ; l + 1 < r; ) {
		mid = l + r >> 1;
		if (getSum(mid))
			l = mid;
		else
			r = mid;
	}
	return l;
}

LL b[MAX_N];

void check(LL x)
{
	int tot = 0;
	LL cost = 0;
	for(int i = 0; i < 37; ++ i) {
		if (a[i] <= x) {
			b[tot ++] = x - a[i];
			cost += x - a[i];
		}
	}
	
	sort(b, b + tot);
	reverse(b, b + tot);
	
	LL sum, per;
	double xx;
	
	for(int i = 1; i <= tot; ++ i) {
		if (cost + tot - i > B) continue;
		per = 36.0 / i;
		sum = 0;
		for(int j = 0; j < i; ++ j) {
			sum += b[j];
		}
		xx = double(sum * 36) / i;
		xx -= cost + (tot - i);
		ret = max(ret, xx);
	}
}

void solve(int test)
{
	printf("Case #%d: ", test);
	memset(a, 0, sizeof a);
	ret = 0;
	cin >> B >> N;
	for(int i = 0; i < N; ++ i)
		cin >> a[i];
	
	M = calc();
	
	if (M) check(M - 1);
	check(M);
	
	for(int i = 0; i < N; ++ i) {
		check(a[i] - 1);
		check(a[i]);
		check(a[i] + 1);
	}
	
	printf("%.10f\n", ret);
}

int main()
{
	//freopen("A.in", "r", stdin); freopen("A.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int testcase; scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) solve(i);
	fclose(stdout);
	return 0;
}
