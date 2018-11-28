#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <stdio.h>
#include <complex>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef pair<int, PII> TIII;
typedef long long LL;
typedef vector<LL> VLL;

//container util

//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define MT(a,b,c) MP(a, MP(b, c))
#define T1 first
#define T2 second.first
#define T3 second.second

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

int board[100][100];
int checked[100][100];
int h,w;

int check(int p, int q){
	memset(checked, 0, sizeof(checked));
	REP(i,h){
		REP(j,w){
			if(checked[i][j]==0 && board[i][j] == p){
				int flag = 1;
				REP(k,w)if(board[i][k]!=p)flag = 0;
				if(flag)REP(k,w)checked[i][k]=1;
				flag = 1;
				REP(k,h)if(board[k][j]!=p)flag = 0;
				if(flag)REP(k,h)checked[k][j]=1;
			}
		}
	}
	REP(i,h){
		REP(j,w){
			if(board[i][j] == p){
				if(checked[i][j] != 1){
					return -1;
				}
				else board[i][j] = q;
			}
		}
	}
	return 0;
}

void solve(int t){
	cin>>h>>w;
	VI v;
	REP(i,h)REP(j,w){
		cin>>board[i][j];
		v.PB(board[i][j]);
	}
	v.PB(100);
	SORT(v);
	unique(ALL(v));
	int imax = v.size()-1;
	REP(i,imax){
		if(-1==check(v[i],v[i+1])){
			printf("Case #%d: NO\n", t+1);
			return;
		}
	}
	printf("Case #%d: YES\n", t+1);
}

void main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin>>T;
	REP(t,T){
		solve(t);
	}
}