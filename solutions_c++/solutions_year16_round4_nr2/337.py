// #includes {{{
#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define LET(x,a) __typeof(a) x(a)
//#define IFOR(i,it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it,++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair

#define EXIST(e,s) ((s).find(e)!=(s).end())

#define RESET(a) memset((a),0,sizeof(a))
#define SET(a) memset((a),-1,sizeof(a))
#define PB push_back
#define DEC(it,command) __typeof(command) it=command

const int INF=0x3f3f3f3f;

typedef long long Int;
typedef unsigned long long uInt;
#ifdef __MINGW32__
typedef double rn;
#else
typedef long double rn;
#endif

typedef pair<int,int> pii;

/*
#ifdef MYDEBUG
#include"debug.h"
#include"print.h"
#endif
*/
// }}}

int N,K;
rn p[205];
rn a[205][205];

rn calc_tie(const vector<rn> &q){
	assert(q.size()==K);
	a[0][0] = 1.0L;
	REP(i,q.size()){
		for(int j=0;j<=i+1;j++){
			rn u = 0.0L;
			if(j>0)u+=a[i][j-1]*q[i];
			if(j<=i)u+=a[i][j]*(1.0L-q[i]);
			a[i+1][j]=u;
		}
	}
	return a[K][K/2];
}

void main2(){
	cin>>N>>K;
	REP(i,N)cin>>p[i];
	sort(p,p+N);
	rn ans = 0.0;
	REP(c,K+1){
		vector<rn> q;
		REP(i,c)q.push_back(p[i]);
		REP(i,K-c)q.push_back(p[N-1-i]);
		rn t = calc_tie(q);
		ans = max(ans,t);
	}
	printf("%.10Lf\n",ans);
}

// main function {{{
int main() {
	int T;cin>>T;
	REP(ct, T){
		cout<<"Case #"<<ct+1<<": ";
		main2();
	}
	return 0;
}
//}}}
