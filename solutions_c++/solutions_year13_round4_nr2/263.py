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

int N;
Int B,P;

Int rank(Int t,Int M){//team, match guaranteed rank
	if(M==0){
		return t;
	}
	if(t==0){
		return 0;
	}else{
		return rank((t-1)/2,M-1)+(1ll<<(M-1));
	}
}

Int rank2(Int t,Int M){//maximum rank
	if(M==0)return t;
	if(t==((1ll<<M)-1)){
		return t;
	}else{
		return rank2((t+1)/2,M-1);
	}
}

void main2(){
	cin>>N>>P;
	P--;
	B=(1ll<<N);
	Int l=0,r=B;
	while(r-l>1){
		Int t=(l+r)/2;
		Int p=rank(t,N);
//		cout<<t<<" "<<p<<endl;
		if(p>P)r=t;
		else l=t;
	}
	Int ans0=l;
	l=0;r=B;
	while(r-l>1){
		Int t=(l+r)/2;
		Int p=rank2(t,N);
		if(p>P)r=t;
		else l=t;
	
	}
	Int ans1=l;
	cout<<ans0<<" "<<ans1<<endl;
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
