/* hanhanw v1.2 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
// for Online Judge or Contests
#define MSET(x,y) memset(x,y,sizeof(x))
#define REP(x,y,z) for(int x=(y); x<=(z); x++)
#define FORD(x,y,z) for(int x=(y); x>=(z); x--)
#define FLST(x,y,z) for(int x=(y); x; x=z[x])
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define SZ(x) ((int)x.size())
#define PB push_back

using namespace std;
//
typedef long long LL;
typedef unsigned long long uLL;
typedef long double LD;
// start here OAO~

int n,p;

LL f1(LL x){
	int rr=0;
	LL l=1, r=1ll<<n;
	LL cnt = x;

	while(cnt && rr<n){
		l = (l+r)/2 + 1;
		cnt = min(r-l, (cnt-1)/2);
		rr++;
	}
	while(rr < n){
		r = (l+r)/2;
		rr++;
	}
	return l<=p;
	
}
LL f2(LL x){
	int rr=0;
	LL l=1, r=1ll<<n;
	LL cnt = r-1-x;
	while(cnt && rr<n){
		r = (l+r)/2;
		cnt = min(r-l, (cnt-1)/2);
		rr++;
	}
	while(rr < n){
		l = (l+r)/2 + 1;
		rr++;
	}
	return l<=p;
}


void solve(int T){
	scanf("%d %d", &n, &p);
	LL l=0,r=1ll<<n;
	LL a1,a2;
	while (l<r){
		LL m=(l+r)>>1;
		if (f1(m)) l = m +1;
		else r=m;
	}
	a1 = l-1;
	l=0; r=1ll<<n;
	while (l<r){
		LL m=(l+r)>>1;
		if (f2(m)) l=m+1;
		else r=m;
	}
	a2 = l-1;
	printf("Case #%d: %I64d %I64d\n", T, a1, a2);
}
int main(int argc, char** argv){
	int nT; scanf("%d", &nT);
	for (int T = 1; T <= nT; T++)
		solve(T);
	return 0;
}

