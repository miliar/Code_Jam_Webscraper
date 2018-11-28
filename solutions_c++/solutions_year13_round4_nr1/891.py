/*
 * A.cpp
 *
 *  Created on: Jun 1, 2013
 *      Author: Marwan
 */

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <climits>
#include <set>
#include <map>

using namespace std;

const int oo = (int)1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
#define MP make_pair
#define SZ(x) (int)x.size()

int dcmp (double a, double b){
	return (fabs(a-b) <= eps) ? 0 : (( a < b ) ? -1 : 1) ;
}

typedef long long ll;
typedef pair<int,int> pii;

struct event {
	int st ;
	int cnt ;
	bool in ;

	event (int station, int count, bool n) {
		st = station ;
		cnt = count ;
		in = n ;
	}

	bool operator< (const event & e) const
	{
		if (st != e.st)
			return st < e.st ;

		return in ;
	}

	void print (){
		cout << "event " << st << " " << cnt << " " << in << endl ;
	}
};

const ll mod = 1000002013ll ;
int main (){
#ifndef ONLINE_JUDGE
	freopen ("in.in", "rt", stdin);
//	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);
#endif
	int T ;
	cin >> T ;


	for (int t=0 ; t < T ; t++)
	{
		cout << "Case #" << t+1 << ": " ;
		int N, M ;
		vector <event> ve ;

		cin >> N >> M ;
		ll cst = 0ll ;
		for (int i=0 ; i < M ; i++)
		{
			int f, t, p ;
			cin >> f >> t >> p ;

			int l = t - f ;
			ll cur = (l*N - (l * (l-1) / 2)) % mod;
			cur *= p ;
			cur %= mod ;

//			cout << f << " " << t << " " << p <<  " - > " << cur << endl ;

			cst += cur ;
			ve.push_back(event(f, p, 1)) ;
			ve.push_back(event(t, p, 0)) ;
		}

		sort (ve.begin(), ve.end()) ;

//		for (int i=0 ; i < SZ(ve) ; i++)
//			ve[i].print();
//
//		cout << "total cost is " << cst << endl ;

		vector <pii> vp ;
		ll mncst = 0ll ;
		for (int i=0 ; i < SZ(ve) ; i++)
		{
//			ve[i].print();

			if (ve[i].in)
			{
				vp.push_back(MP(ve[i].st, ve[i].cnt)) ;
			}
			else
			{
				while (SZ(vp) && ve[i].cnt) {
					pii c = vp.back() ;
//					cout << "while " << c.first << " " << c.second << endl ;
					vp.pop_back() ;

					ll canleave = min (ve[i].cnt, c.second) ;

//					cout << "can leave " << canleave << endl ;
					int l = ve[i].st - c.first ;

//					cout << "len is " << l << endl ;
					ll cur = (l*N - (l * (l-1) / 2)) % mod;
					cur *= canleave ;
					cur %= mod ;
//
//					cout << "cur is " << cur << endl ;
 					mncst += cur ;
					mncst %= mod ;

					c.second -= canleave ;
					ve[i].cnt -= canleave ;

					if (c.second > 0)
						vp.push_back(c) ;
				}
			}
		}

		cout << cst - mncst << endl ;
	}
	return 0;
}
