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
long long b[51];
long long Ihave;

bool check(int pos, long long each)
{
	long long needs = 0;
	for(int i = 1; i <= pos; i++)
	{
		if(b[i] > each)
			return false;
		needs += each - b[i];
	}
	for(int i = pos+1; i <= 37; i++)
		if(b[i] < each + 1)
			needs += each + 1 - b[i];
	return needs <= Ihave;
}

long long realPay(int pos, long long each)
{
	long long needs = 0;
	for(int i = 1; i <= pos; i++)
	{
		if(b[i] > each)
			return false;
		needs += each - b[i];
	}
	for(int i = pos+1; i <= 37; i++)
		if(b[i] < each + 1)
			needs += each + 1 - b[i];
	return needs;
}

double calc2(int pos)
{
	long long total = 0;
	for(int i = 1; i <= pos; i++)
		total += b[i];
	long long maxEach = (total + Ihave) / pos;


	if(pos < 37)
		maxEach = min(maxEach, b[pos+1] - 1);
	if(maxEach < b[pos]) return 0;
	long long Ipay = maxEach * pos - total;
	//cout << Ipay << endl;
	if(Ipay > Ihave) return 0;

	double Iget = 36.0 / pos * Ipay;
	return Iget - Ipay;
}

double calc(int pos)
{
	long long L = 0, R = Ihave + 1, M;
	while(R - L > 1)
	{
		M = (L + R) / 2;
		if(check(pos, M) == false)
			R = M;
		else
			L = M;
	}
	long long maxEach = L;
	long long total = 0;
	for(int i = 1; i <= pos; i++)
		total += b[i];
	long long Ipay = maxEach * pos - total;
	//cout << Ipay << endl;

	double Iget = 36.0 / pos * Ipay;
	return Iget - realPay(pos, L);
}

void solve()
{
	cin >> Ihave;
	cin >> n;
	memset(b, 0, sizeof(b));
	for(int i = 1; i <= n; i++)
		cin >> b[i];
	sort(b + 1, b + 1 + 37);
	double ans = 0;

	for(int i = 1; i <= 36; i++)
	{
		//cout << i << ": " << calc(i) << endl;
		ans = max(ans, calc(i));
		ans = max(ans, calc2(i));
	}
	cout << ans << endl;
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
