/*
 * D.cpp
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
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.in.out.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		int n;
		cin>>n;
		vector<int> Naomi, Ken;

		lp(i, n)
		{
			double d;
			cin>>d;
			Naomi.push_back(d * 1e7);
		}

		lp(i, n)
		{
			double d;
			cin>>d;
			Ken.push_back(d * 1e7);
		}


		sort(all(Naomi));
		sort(all(Ken));

		vector<int> Naomi2 = Naomi, Ken2 = Ken;

		int ans1 = 0;
		lp(i, n)
		{
			vector<int>::iterator it = upper_bound(all(Naomi), Ken[i]);
			if(it != Naomi.end())
			{
				ans1++;
				Naomi.erase(it);
			}
		}

		Naomi = Naomi2;
		Ken = Ken2;

		int ans2 = 0;
		lp(i, n)
		{
			vector<int>::iterator it = upper_bound(all(Ken), Naomi[i]);

			if(it == Ken.end())
			{
				ans2++;
				Ken.erase(Ken.begin());
			}
			else
				Ken.erase(it);
		}

		printf("Case #%d: %d %d\n", cc+1, ans1, ans2);
	}

	return 0;
}
