#include <algorithm>
#include <iostream>
#include <iomanip>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

int n;
long long x[1000001];
long long s[1000001];
long long P,Q,R,S;

long long calc(int L, int R)
{
	return s[R] - s[L-1];
}

int searchL(long long limit)
{
	if(calc(1, n) <= limit) return n;
	int L = 0, R = n, M;
	while(R - L > 1)
	{
		M = (L + R) / 2;
		if(calc(1, M) <= limit)
			L = M;
		else
			R = M;
	}
	return L;
}

int searchR(long long limit)
{
	if(calc(1, n) <= limit) return 1;
	int L = 1, R = n+1, M;
	while(R - L > 1)
	{
		M = (L + R) / 2;
		if(calc(M, n) <= limit)
			R = M;
		else
			L = M;
	}
	return R;
}

bool check(long long limit)
{
	int L = searchL(limit) + 1;
	int R = searchR(limit) - 1;
	if(L > R) return true;
	return calc(L, R) <= limit;
}

void solve()
{
	cin >> n;
	cin >> P >> Q >> R >> S;
	long long sum = 0;
	s[0] = 0;
	for(int i = 1; i <= n; i++)
	{
		x[i] = ((i-1) * P + Q) % R + S;
		sum += x[i];
		s[i] = s[i-1] + x[i];
	}
	long long L = 0, R = sum+1, M;
	while(R - L > 1)
	{
		M = (L + R) / 2;
		if(check(M))
			R = M;
		else
			L = M;
	}
	cout << 1 - 1.0 * R / sum << endl;
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	//srand((unsigned)time(NULL));
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	return MAIN();
}
