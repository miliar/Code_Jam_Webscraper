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

const int MAX_N = 100000 + 10;

LL N, P, S;

int check1(LL x)
{
	LL k = 0, tmp = 1;
	++ x;
	for( ; ; ) {
		tmp *= 2;
		if (x < tmp) break;
		++ k;
	}
	return (S - (1LL << (N - k)) + 1) <= P;
}

int check2(LL x)
{
	x = S - x;
	LL tmp = S / 2, ret = S, checkx = 2;
	for( ; ; ) {
		if (x < checkx) break;
		ret -= tmp;
		checkx *= 2;
		tmp /= 2;
	}
	return (ret <= P);
}

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> N >> P;
	S = (1LL << N);
	
	LL l = 0, r = S, mid;
	for( ; l + 1 < r; ) {
		mid = (l + r) / 2;
		if (check1(mid))
			l = mid;
		else
			r = mid;
	}
	
	cout << l << ' ';
	
	l = 0, r = S, mid;
	for( ; l + 1 < r; ) {
		mid = (l + r) / 2;
		if (check2(mid))
			l = mid;
		else
			r = mid;
	}
	
	cout << l << endl;
}

int main()
{
	//freopen("B.in", "r", stdin); freopen("B.out", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out2", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out2", "w", stdout);
	int testcase; scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) solve(i);
	fclose(stdout);
	return 0;
}
