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

int n, m, a[104][104], p[104][104];

const int DX[2] = {0,1};
const int DY[2] = {1,0};

bool maxAltura(int i, int j){
	int ma = a[i][j];
	bool reti = true, retj = true;
	
	forn(y,m) if(a[i][y] > ma)
		reti = false;
	forn(x,n) if(a[x][j] > ma)
		retj = false;
	
	return reti || retj;
}

bool gana(){
	forn(i,n) forn(j,m) if(!p[i][j]){
		if(!maxAltura(i,j))
			return false;
	}
	return true;
}

int main()
{
#ifdef __YO__
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	
	int T;
	cin >> T;
	
	forn(t, T){
		cin >> n >> m;
		forn(i,n) forn(j,m) cin >> a[i][j];
		memset(p,0,sizeof(p));
		
		forn(i, n){
			int val = a[i][0];
			bool pasa = true;
			forn(j,m)
				pasa &= val == a[i][j];
			if(pasa){
				forn(j,m)
					p[i][j] = 1;
			}
		}
		forn(j, m){
			int val = a[0][j];
			bool pasa = true;
			forn(i,n)
				pasa &= val == a[i][j];
			if(pasa){
				forn(i,n)
					p[i][j] = 1;
			}
		}
		
		if(gana())
			printf("Case #%i: YES\n", t+1);
		else
			printf("Case #%i: NO\n", t+1);
	}

	return 0;
}
