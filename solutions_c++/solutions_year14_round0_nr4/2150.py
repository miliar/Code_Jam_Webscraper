#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <set>
#include <cctype>
#include <algorithm>
#include <climits>
#include <queue>
#include <functional>
#include <map>

#define FOREACH(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define REP(i,n) FOR(i,0,n)
#define REPN(i,n) FORN(i,1,n)

#define ALL(c) (c).begin(), (c).end()
#define F first
#define S second
#define INS insert
#define MP make_pair
#define PB push_back
#define LL long long
#define ULL unsigned long long

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

template <class T> inline T MAX(T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN(T a, T b) { if (a < b) return a; return b; }
template <class T> inline T ABS(T x) { if (x < 0) return -x; return x; }

inline void OPEN(const string &s) {
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

const static int inf = 1000000000;

#define MAXN 1005

int n,t;
double a[MAXN],b[MAXN];
double c[MAXN],d[MAXN];

bool asc(double a,double b){
	return a < b;
}

bool desc(double a,double b){
	return a > b;
}

int cal1(){
	memcpy(c,a,sizeof(a));
	memcpy(d,b,sizeof(b));
	sort(c,c+n,desc);
	sort(d,d+n,desc);
	int i = 0,j=0;
	while(i < n && j < n){
		while(c[i] < d[j]) j++;
		if(j >= n) break;
		i++;
		j++;
	}
	return i;
}

int cal2(){
	memcpy(c,a,sizeof(a));
	memcpy(d,b,sizeof(b));
	
	sort(c,c+n,asc);
	sort(d,d+n,asc);
	
	int i=0,j=0;
	while(i < n && j < n){
		while(c[i] > d[j]) j++;
		if(j >= n) break;
		i++;
		j++;
	}
	return n-i;
}

int main(){
	OPEN("D-large");
	scanf("%d",&t);
	REPN(tc,t){
		scanf("%d",&n);
		REP(i,n) scanf("%lf",&a[i]);
		REP(i,n) scanf("%lf",&b[i]);
		printf("Case #%d: %d %d\n",tc,cal1(),cal2());
	}
	return 0;
}

