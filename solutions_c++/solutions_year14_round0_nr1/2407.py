/*
 * A.cpp
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
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.in.out.txt", "wt", stdout);
#endif

	int cases;

	scanf("%d", &cases);

	lp(cc, cases)
	{
		vector< vector<int> > v1(4, vector<int>(4));
		vector< vector<int> > v2(4, vector<int>(4));
		int r1, r2;

		scanf("%d", &r1);
		lp(i, 4) lp(j, 4)	scanf("%d", &v1[i][j]);

		scanf("%d", &r2);
		lp(i, 4) lp(j, 4)	scanf("%d", &v2[i][j]);

		r1--, r2--;
		sort(all(v1[r1]));
		sort(all(v2[r2]));

		vector<int> v;

		set_intersection(all(v1[r1]), all(v2[r2]), back_inserter(v));

		if(sz(v) == 0)
			printf("Case #%d: Volunteer cheated!\n", cc+1);
		else if(sz(v) == 1)
			printf("Case #%d: %d\n", cc+1, v[0]);
		else
			printf("Case #%d: Bad magician!\n", cc+1);
	}


	return 0;
}
