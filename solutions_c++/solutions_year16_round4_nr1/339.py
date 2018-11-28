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

vector<int> build(int n, int winner){
	int loser = (winner+1)%3;
	if(n==0){
		vector<int> v;
		v.push_back(winner);
		return v;
	}
	vector<int> v = build(n-1,winner), w = build(n-1,loser);
	REP(i,w.size())v.push_back(w[i]);
	return v;
}

string tostring(const vector<int> &v){
	string s = "";
	REP(i,v.size()){
		if(v[i]==0)s+='R';
		else if(v[i]==1)s+='S';
		else if(v[i]==2)s+='P';
		else assert(false);
	}
	return s;
}

string alphabetical(const string &s,int n){
	if(n==0)return s;
	const int b = (1<<(n-1));
	string s0 = alphabetical(s.substr(0,b),n-1), s1 = alphabetical(s.substr(b,b),n-1);
	if(s0<=s1)return s0+s1;
	else return s1+s0;

}

vector<int> t(3);

void main2(){
	int N;
	cin>>N;
	cin>>t[0]>>t[2]>>t[1];
	vector<int> v = build(N,0);
	string ans = "Z";
	REP(i,3){
		vector<int> u(3);
		REP(j,v.size()){
			u[v[j]]++;
		}
		if(u[0]==t[0] and u[1]==t[1] and u[2]==t[2]){
			string ans2 = alphabetical(tostring(v),N);
			if(ans2<ans)ans=ans2;
		}
		REP(j,v.size())v[j]=(v[j]+1)%3;
	}
	if(ans=="Z"){
		cout<<"IMPOSSIBLE"<<endl;
	}else{
		cout<<ans<<endl;
	}
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
