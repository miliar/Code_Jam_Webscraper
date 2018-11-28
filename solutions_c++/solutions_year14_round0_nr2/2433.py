/*
 * B.cpp
 *
 *  Created on: Apr 12, 2014
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

int main()
{
#ifndef ONLINE_JUDGE
	//freopen("c.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.in.out.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		double c, f, x;
		cin>>c>>f>>x;

		double curTime = 0;
		double rate = 2;
		double ans = x / rate;

		if(dcmp(f, 0) != 0)
		{
			for(int s = 0; s < 2*1e6; ++s)
			{
				// use available
				double remaining = x / rate;
				ans = min(ans, curTime + remaining);

				// add new farm
				double newFarmTime = c / rate;

				curTime += newFarmTime;
				rate += f;
			}
		}

		if(dcmp(x, 0) == 0)
			ans = 0;

		printf("Case #%d: %.7lf\n", cc+1, ans);
	}

	return 0;
}
