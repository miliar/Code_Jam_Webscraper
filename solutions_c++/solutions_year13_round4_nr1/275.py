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

const int mod=1000002013;

int N,M;
int o[1010],e[1010],p[1010];

struct S{
	bool ride;
	int x,n;
	S(int x,int n,bool b):ride(b),x(x),n(n){}
	bool operator<(const S &s)const{
		if(x!=s.x)return x<s.x;
		else{
			if(ride!=s.ride)return ride;
			else return false;
		}
	}
};

Int fee(Int d){
	if(d==0)return 0;
	return d*(Int)(N*2-d+1)/2;
}

void main2(){
	cin>>N>>M;
	REP(i,M){
		cin>>o[i]>>e[i]>>p[i];
	}
	Int cost0=0;
	REP(i,M){
		if(o[i]==e[i])continue;
		Int d=abs(o[i]-e[i]);
		cost0+=fee(d)%mod*p[i]%mod;cost0%=mod;
	}
	Int cost1=0;
	do{
		vector<S> v;
		REP(i,M){
			if(o[i]<e[i])v.push_back(S(o[i],p[i],true)),v.push_back(S(e[i],p[i],false));
		}
		sort(ALL(v));
		/*
		REP(i,v.size()){
			cout<<v[i].x<<" "<<v[i].ride<<endl;
		}
		break;
		*/
		vector<pii> s;
		REP(i,v.size()){
			/*
			cout<<"s: ";
			REP(j,s.size())cout<<s[j].first<<","<<s[j].second<<" ";
			cout<<endl;
			*/
			if(v[i].ride){
				s.push_back(make_pair(v[i].x,v[i].n));
			}else{
				int u=v[i].n;
				while(u>0){
					pii p=s.back();
					if(u>=p.second){
						u-=p.second;
						cost1+=fee(abs(v[i].x-p.first))%mod*p.second%mod;
						cost1%=mod;
						s.pop_back();
					}else{
						s.back().second-=u;
						cost1+=fee(abs(v[i].x-p.first))%mod*u%mod;
						cost1%=mod;
						u=0;
						break;
					}
				}
			}
		}
	}while(0);
//	cout<<cost0<<" "<<cost1<<endl;
	cout<<(cost0-cost1%mod+mod)%mod<<endl;
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
