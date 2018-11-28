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

int R,C;
char a[110][110];

bool inner(int i,int j){
	return i>=0 and i<R and j>=0 and j<C;
}

string ds = "^>v<";
int dir[4][2]={{-1,0},{0,1},{1,0},{0,-1}};

void main2(){
	cin>>R>>C;
	REP(i,R)cin>>a[i];
	int ans = 0;
	REP(i,R){
		REP(j,C){
			if(a[i][j]=='.')continue;
			vector<bool> f;
			REP(d,4){
				int i0 = i, j0 = j;
				bool found = false;
				while(1){
					i0+=dir[d][0];
					j0+=dir[d][1];
					if(not inner(i0,j0))break;
					if(a[i0][j0]!='.'){
						found = true;
					}
				}
				f.push_back(found);
			}
			if(not f[0] and not f[1] and not f[2] and not f[3]){
				cout<<"IMPOSSIBLE"<<endl;
				return;
			}
			bool valid = false;
			REP(k,4){
				if(a[i][j]==ds[k]){
					if(f[k])valid=true;
				}
			}
			if(valid)continue;
			else ans++;
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
