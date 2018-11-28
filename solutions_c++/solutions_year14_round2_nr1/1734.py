/*
 * A.cpp
 *
 *  Created on: May 3, 2014
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
const ll OO = 1e8;

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

pair<string, vector< pair<char, int> > > split(string s)
{
	vector< pair<char, int> > v;

	char last = '@';
	int cnt = 0;
	string cleaned = "";

	rep(i, s)
	{
		if(s[i] != last)
		{
			if(cnt)
			{
				v.push_back(make_pair(last, cnt));
				cleaned += last;
			}
			last = s[i];
			cnt = 1;
		}
		else
			cnt++;
	}

	v.push_back(make_pair(last, cnt));
	cleaned += last;

	return make_pair(cleaned, v);
}

int calc(vector<int> f)
{
	sort(all(f));
	int mn = f[0];
	int mx = f.back();

	int ret = 1e8;

	lpi(i, mn, mx+1)
	{
		int sum = 0;

		rep(j, f)
			sum += abs(i - f[j]);

		ret = min(ret, sum);
	}

	return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
	//freopen("c.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.in.out.txt", "wt", stdout);
#endif

	int cases;

	cin>>cases;

	lp(cc, cases)
	{
		int n;
		cin>>n;
		set<string> allS;
		vector<  vector< pair<char, int> > > v;

		lp(i, n)
		{
			string s;
			cin>>s;

			pair<string, vector< pair<char, int> > > p = split(s);
			allS.insert(p.first);
			v.push_back(p.second);
		}

		if(sz(allS) > 1)
		{
			printf("Case #%d: Fegla Won\n", cc+1);
			continue;
		}
		string best = *allS.begin();

		int ans = 0;
		rep(i, best)
		{
			vector<int> f;
			rep(j, v)
				f.push_back(v[j][i].second);

			ans += calc(f);
		}

		printf("Case #%d: %d\n", cc+1, ans);
	}

	return 0;
}
