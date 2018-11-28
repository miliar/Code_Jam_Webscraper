/*
 * B.cpp
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

ll N, P ;

ll wrst (ll x)
{
	ll cnt = x ;
	ll res = 0 ;

	for (int i=0 ; i <= N ; i++)
	{
		if (i)
			cnt = (cnt - 1) / 2 ;

		if (cnt > 0)
			res |= (1ll << (N - 1 - i));
	}
	return res ;
}

ll bst (ll x)
{
	ll cnt = (1 << N) - x - 1;
	ll res = 0 ;

	for (int i=0 ; i < N ; i++)
	{
		if (i)
			cnt = (cnt - 1) / 2 ;

		if (cnt == 0){
			res |= (1ll << (N - 1 - i));
		}
	}
	return res ;
}

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

		cin >> N >> P ;

		int rnk1 = -1 ;

		int rnk2 = -1 ;

		for (int i=0 ; i < (1 << N) ; i++)
		{
			int b = bst(i) ;
			int w = wrst(i) ;

			if (w < P){
				rnk2 = i ;
			}

			if (b < P)
				rnk1 = i ;
		}

		cout << rnk2 << " " << rnk1 << endl ;
	}
	return 0;
}

//
//
//ll bestrank (ll x)
//{
//	ll cnt = x ;
//	ll cnt2 = (1ll << N) - x ;
//	for (int i=0 ; i < N ; i++)
//	{
//		cnt = (cnt+1)/2 ;
//		cnt2 /= 2;
//		if (cnt2 == 0)
//			return cnt ;
//	}
//
//	return cnt;
//}
//
//ll worstrank (ll x)
//{
//	ll cnt2 = x - 1 ;
//	ll cnt = (1ll << N) - x ;
//	for (int i=0 ; i < N ; i++)
//	{
//		cnt = (cnt+1)/2 ;
//		cnt2 /= 2;
//		if (cnt2 == 0)
//			return cnt ;
//	}
//
//	return cnt ;
//}

