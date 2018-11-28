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

bool visited[5];
bool is_valid(const vector<vector<int> > &a){
	memset(visited,false,sizeof(visited));
	int n = a.size();
	REP(i,n){
		if(visited[i])continue;
		visited[i]=true;
		set<int> ones;
		REP(j,n){
			if(a[i][j]==1)ones.insert(j);
		}
		set<int> s;
		for(int k=i+1;k<n;k++){
			FOR(it,ones){
//			REP(j,ones.size()){
				if(a[k][*it]==1){
					s.insert(k);
					visited[k]=true;
					break;
				}
			}
		}
		if(s.size()+1!=ones.size())return false;
		FOR(it,s){
			REP(j,n){
				if(ones.find(j)!=ones.end())if(a[*it][j]==0)return false;
				if(ones.find(j)==ones.end())if(a[*it][j]==1)return false;
			}
		}
	}
		/*
	cout<<"==="<<endl;
	REP(i,a.size()){
		REP(j,a.size())cout<<a[i][j]<<" ";
		cout<<endl;
	}
	cout<<"==="<<endl;
	*/
	return true;
}

void main2(){
	int N;
	cin>>N;
	vector<vector<int> > a(N,vector<int>(N));
	REP(i,N){
		string s;
		cin>>s;
		REP(j,N){
			if(s[j]=='0')a[i][j]=0;
			else if(s[j]=='1')a[i][j]=1;
			else assert(false);
		}
	}
	vector<pii> v;
	REP(i,N)REP(j,N)if(a[i][j]==0)v.push_back(MP(i,j));
	int B = (1<<v.size());
	int ans = INF;
	REP(b,B){
		int ct = 0;
		REP(i,v.size())if(b&(1<<i)){
			assert(a[v[i].first][v[i].second]==0);
			a[v[i].first][v[i].second]=1;
			ct++;
		}
		if(is_valid(a)){
			ans=min(ans,ct);
		}

		REP(i,v.size())if(b&(1<<i)){
			assert(a[v[i].first][v[i].second]==1);
			a[v[i].first][v[i].second]=0;
		}
	}
	cout<<ans<<endl;
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
