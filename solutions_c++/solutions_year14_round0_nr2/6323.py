// File Name   : cookie.cpp
// Development : Sat Apr 12 11:18:10 2014
// Author      : Vishwakarma

#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <set>
#include <float.h>
#include <new>
#include <sstream>
#include <complex>
#include <deque>

#define TR(c,i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define SWAP(a,b) {typeof(a) T; T=a; a=b; b=T;}
#define FOR(i,a,b) for ( i = a; i <= b; i++ )
#define ROF(i,a,b) for ( i = a; i >= b; i-- )
#define MEM(t,n) ( t * )malloc( (n)*sizeof( t ) )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define MAX(a,b) ((a) >= (b) ? (a) : (b))
#define MIN(a,b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SET(x,a) memset(x,a,sizeof(x))
#define IN(x,a) x.find(a) != x.end()  
#define SQ(x) (x)*(x)
#define DIST(x1,y1,x2,y2) SQ(x1-x2)+SQ(y1-y2)
#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

int main()
{
	int T;
	double C, F, X;
	cin >> T;
	for(int i=1;i<=T;i++){
		cin >>  C >> F >> X;
		double ans = 0;
		double rate = 2.0;
		bool done = false;
		while(!done){
			if(X/rate <= (C/rate + X/(rate+F))){
				ans += X/rate;
				done = true;	
			}
			else{
				ans += C/rate;
				rate += F;
			}
		}
		cout << "Case #"<<i<<": ";
		printf("%0.7f\n",ans);
	}
	return 0;
}

