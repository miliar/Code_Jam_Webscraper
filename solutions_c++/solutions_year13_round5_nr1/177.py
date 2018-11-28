#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker,"/STACK:267386880")

#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <cstdlib>
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
#define MOD 1000000007
#define PRIME 1000003

using namespace std;

void solve(LL b, LL n, vector< LL > &d)
{
	double ans(0.);
	while (sz(d)!=37)
		d.push_back(0);
	sort(all(d));
	int ind(0);
	vector<LL> pay(37);
	while (ind<sz(d)-1 && d[ind]==d[ind+1])
		++ind;
	rept(hm,b)
	{
		d[ind]+=1;
		pay[ind]++;
		--ind;
		double win(0);
		int smth=0;
		while (smth<sz(d)-1 && d[smth]==d[smth+1])
			++smth;
		int ww=smth+1;
		rept(i,ww)
			win+=pay[i]*1./ww*36;
		win-=hm+1;
		ans=max(ans,win);
		if (ind<0)
			ind=smth;
	}
	printf("%.8lf\n",ans);
	/*int k(0);
	while (sz(d) != 37)
	{
		++k;
		d.push_back(1);
		--b;
	}
	sort(all(d));
	int hm(1);
	while (hm<sz(d) && d[hm-1]==d[hm])
		++hm;
	double ans(max(0.,k*1./hm*));
	rept(i,36)
	{
		int beton=i+1;
		FOR(hm,1,b/beton)
		{

		}
	}*/
	/*while (sz(d) != 37)
		d.push_back(0);
	sort(all(d));
	int hm(1);
	while (hm<sz(d) && d[hm]==d[hm-1])
		++hm;
	double ans(-1);
	rept(i,hm)
	{
		int beton=hm;
		int howP=b/beton;
		ans = max(ans, beton*1./hm * howP * 36 - beton * howP);
	}
	if (ans<0.0)
		ans=0;
	printf("%.7lf\n",ans);*/
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
		long long b,n;
		cin>>b>>n;
		vector< LL > d(n);
		rept(i,n)
			cin>>d[i];
		printf("Case #%d: ",t+1);
		solve(b,n,d);
	}
	return 0;
}