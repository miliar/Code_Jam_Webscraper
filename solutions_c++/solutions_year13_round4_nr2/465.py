#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

bool ganoSeguro(tint n, tint p, tint rank){
	tint r = rank;
	tint ls = 0;

	while(r > 0){
		ls++;
		r = (r-1LL)/2LL;
	}

	forn(i, ls)
		p -= (1LL<<(n-i-1LL));
	return p > 0;
}

bool ganoQuizas(tint n, tint p, tint rank){
	tint l = (1LL<<n)-rank-1;
	tint ws = 0;
	
	while(l > 0){
		ws++;
		l = (l-1LL)/2LL;
	}
	
	//cout << ws << endl;
	
	p -= (1LL<<(n-ws)) - 1LL;
	
	return p > 0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	cin >> T;
	
	forn(t, T){
		tint n; tint p;
		cin >> n >> p;
		tint eleSeg=0, eleCoul=0; 
		
		//cout << ganoSeguro(n,p,1) << endl;
		tint mi = 0, ma = (1LL<<n)-1LL, mid;
		while(mi <= ma){
			mid = (mi+ma)/2LL;
			
			if(ganoSeguro(n,p,mid)){
				eleSeg = mid;
				mi = mid+1LL;
			}else
				ma = mid-1LL;
		}
		
		//cout << ganoQuizas(n,p,6) << endl;
		mi = 0; ma = (1LL<<n)-1LL;
		while(mi <= ma){
			mid = (mi+ma)/2LL;
			
			if(ganoQuizas(n,p,mid)){
				eleCoul = mid;
				mi = mid+1LL;
			}else
				ma = mid-1LL;
		}
		
		printf("Case #%i: %lld %lld\n", t+1, eleSeg, eleCoul);
	}
	
	return 0;
}
