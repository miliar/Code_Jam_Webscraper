/*
 * A.cpp
 *
 *  Created on: May 12, 2013
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


string vv = "aeiou";

bool vowels(char c)
{
	return (int)vv.find(c) != -1;
}

const int MAX = 1000009;
int arr[MAX];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		string line;
		ll n;
		cin>>line>>n;
		ll k = sz(line);
		rep(i, line)	arr[i] = !vowels(line[i]);
		arr[k] = 0;
		lpd(i, k-1, 0)
		{
			if(arr[i] != 0)
				arr[i] += arr[i+1];
		}

		int last = -1;
		lpd(i, k-1, 0)
		{
			if(arr[i] >= n)
				last = arr[i] = i;
			else
				arr[i] = last;
		}

		ll ans = 0;

		lp(i, k)
		{
			if(arr[i] == -1)
				break;

			ans += k - ((ll)arr[i] + n - 1);
		}

		cout<<"Case #"<<cc+1<<": "<<ans<<"\n";

	}


	return 0;
}
