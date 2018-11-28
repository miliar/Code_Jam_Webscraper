/*
 * A.cpp
 *
 *  Created on: May 4, 2013
 *      Author: Mostafa Saad
 */



#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)

typedef long long         ll;

const double EPS = (1e-7);
int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}

#define pb					push_back
#define MP					make_pair
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
typedef long double   	  ld;
typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;


typedef pair<pair<int, int>, ll> ENTRY;

map<ENTRY, int> mp;
vector<ll> v;

const int OO = (int)1e8;

int best(int i, int soFar, ll cur)
{
	if(i == sz(v))
		return 0;

	if(cur > v[i])
		return best(i+1, 0, cur+v[i]);

	if(soFar > sz(v))
		return OO;

	ENTRY p = make_pair(make_pair(i, soFar), cur);

	if(mp.count(p))
		return mp[p];

	int x = 1 + best(i, soFar+1, cur+cur-1);

	x = min(x, sz(v)-i);

	return mp[p] = x;
}


int main()
{
//	freopen("c.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.in.txt", "wt", stdout);

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		mp.clear();
		ll my;
		int n;
		cin>>my>>n;
		v.clear();
		v = vector<ll>(n);
		rep(i, v)
			cin>>v[i];

		sort(all(v));

		int steps = best(0, 0, my);


		printf("Case #%d: %d\n", cc+1, steps);
	}


	return 0;
}
