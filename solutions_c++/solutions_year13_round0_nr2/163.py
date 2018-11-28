/*
 * C.cpp
 *
 *  Created on: Apr 13, 2013
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
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
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
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out.txt", "wt", stdout);


	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		int n, m;
		cin>>n>>m;

		vector< vector<int> > v(n, vector<int>(m));
		vector<int> maxRow(n, 0);
		vector<int> maxCol(m, 0);

		lp(i, n) lp(j, m) {
			cin>>v[i][j];
			maxRow[i] = max(maxRow[i], v[i][j]);
			maxCol[j] = max(maxCol[j], v[i][j]);
		}

		bool ok = 1;
		lp(i, n) lp(j, m)
			ok &= v[i][j] == maxRow[i] || v[i][j] == maxCol[j];

		printf("Case #%d: %s\n", cc+1, ok ? "YES" : "NO");
	}



	return 0;
}
