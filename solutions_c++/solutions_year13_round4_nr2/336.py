#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker,"/STACK:267386880")

#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>
#include <complex>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1000000000
#define PI 3.141592653589
#define eps 0.00000000001
#define MOD 1000002013
#define PRIME 1000003

using namespace std;

map<pair< LL, LL >, LL> dyn;
map<pair< LL, LL >, LL> gyn;

LL findDyn(LL number, LL count)
{
	if (count == 1 || number == 0)
		return 1;

	if (dyn.count(mp(number,count)))
		return dyn[mp(number,count)];
	
	LL newNum = (number - 1) / 2;
	LL newCount = count/2;

	return dyn[mp(number,count)] = count / 2 + findDyn(newNum, newCount);
}

LL findGyn(LL number, LL count)
{
	if (count == 1 || number == 0)
		return 1;

	if (number == count - 1)
		return count;

	if (gyn.count(mp(number,count)))
		return gyn[mp(number,count)];
	
	LL newCount = count/2;
	LL newNum = newCount - (count - number - 2) / 2 - 1;

	return gyn[mp(number,count)] = findGyn(newNum, newCount);
}

bool can1(LL cur, LL number, LL prizes)
{
	return findDyn(cur,number) <= prizes;
}

bool can2(LL cur, LL number, LL prizes)
{
	return findGyn(cur,number) <= prizes;
}

void solve()
{
	int n;
	LL p;
	cin>>n>>p;
	LL teams = ((1ll)<<n);
	LL BAD = 0, GOOD = teams - 1;
	while (GOOD - BAD > 1)
	{
		LL med = (BAD + GOOD) / 2;
		if (can1(med, teams, p))
			BAD = med;
		else
			GOOD = med;
	}
	LL ans1 = -1;
	if (can1(GOOD, teams, p))
		ans1 = GOOD;
	else
		ans1 = BAD;

	BAD = 0, GOOD = teams - 1;
	while (GOOD - BAD > 1)
	{
		LL med = (BAD + GOOD) / 2;
		if (can2(med, teams, p))
			BAD = med;
		else
			GOOD = med;
	}
	LL ans2 = -1;
	if (can2(GOOD, teams, p))
		ans2 = GOOD;
	else
		ans2 = BAD;
	printf("%lld %lld\n",ans1,ans2);
}

int main()
{
#ifndef ONLINE_JUDGE
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
#endif
	int tst;
	scanf("%d",&tst);
	rept(t,tst)
	{
		printf("Case #%d: ",t+1);
		solve();
	}
	return 0;
}