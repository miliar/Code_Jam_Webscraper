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

int t;
int x;
int arr[6][6];
int c[20]={};
int main(){
	OPEN("A-small-attempt0");
	scanf("%d",&t);
	REPN(tc,t){
		memset(c,0,sizeof(c));
		REP(i,2){
			scanf("%d",&x);
			REPN(j,4) REP(k,4)
				scanf("%d",&arr[j][k]);
			REP(j,4) c[arr[x][j]]++;
		}
		int res=0,idx;
		REPN(i,16) if(c[i] == 2){
			res++;
			idx=i;
		}
		printf("Case #%d: ",tc);
		if(res == 1) printf("%d\n",idx);
		else printf("%s\n",res == 0 ? "Volunteer cheated!" : "Bad magician!");
	}
	return 0;
}

