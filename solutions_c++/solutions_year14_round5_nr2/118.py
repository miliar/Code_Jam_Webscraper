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
int myAtk, towerAtk;
int hp[101], G[101];
int cnt1[101], cnt2[101];
int towerNeed[101];
long long F[101][1001][1001];

long long f(int cur, int myTimes, int towerTimes)
{
	if(myTimes > towerTimes + 1) return -1000000000000000000;
	if(cur == n+1) return 0;
	long long &ret = F[cur][myTimes][towerTimes];
	if(ret != -1) return ret;
	ret = 0;
	ret = max(ret, f(cur+1, myTimes, towerTimes + towerNeed[cur]));
	ret = max(ret, G[cur] + f(cur+1, myTimes + cnt1[cur], towerTimes + cnt2[cur]));
	return ret;
}

void solve()
{
	cin >> myAtk >> towerAtk >> n;
	for(int i = 1; i <= n; i++)
		cin >> hp[i] >> G[i];
	for(int i = 1; i <= n; i++)
	{
		cnt1[i] = (hp[i] / myAtk) + (hp[i] % myAtk > 0);
		cnt2[i] = 0;
		towerNeed[i] = (hp[i] / towerAtk) + (hp[i] % towerAtk > 0);
		for(int u = 1; u <= 10; u++)
			for(int v = 1; v <= 10; v++)
				if(u * myAtk + v * towerAtk >= hp[i])
					if((u-1) * myAtk + v * towerAtk < hp[i])
						if(u - v < cnt1[i] - cnt2[i])
						{
							cnt1[i] = u;
							cnt2[i] = v;
						}
	}
	memset(F, 0xff, sizeof(F));
	cout << f(1, 0, 0) << endl;
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
