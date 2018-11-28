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
#include <cstdint>

#define M_PI       3.14159265358979323846

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
typedef unsigned long long ULL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;

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
#define MOD 1000000007

VS board;
int visit[111][111];
int r,c;
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int setdxdy(char c){
	switch(c){
	case '^':
		return 3;
	case 'v':
		return 1;
	case '>':
		return 0;
	case '<':
		return 2;
	}
}

int DFS1(int p, int q, int d, int cnt){
	visit[p][q] = 1;
	int i=p+dy[d];
	int j=q+dx[d];
	while(i!=-1 && i!= r && j != -1 && j!= c){
		if(visit[i][j])return 0;
		if(board[i][j]!='.'){
			return DFS1(i,j,setdxdy(board[i][j]),cnt+1);
		}
		i+=dy[d];
		j+=dx[d];
	}
	if(cnt == 0)return -1;
	else return 1;
}


int DFS0(int p,int q){
	visit[p][q] = 1;
	int k = setdxdy(board[p][q]);
	REP(i,4){
		int ret = 1;
		int flag = 0;
		if(i==0)ret = 0;
		int tmp = DFS1(p,q,(k+i)%4,0);
		if(tmp != -1)return tmp+(i!=0);
	}
	return -1;
}

void solve(){
	memset(visit, 0, sizeof(visit));
	scanf("%d%d", &r, &c);
	board=VS(r);
	REP(i,r)cin>>board[i];
	int ret = 0;
	REP(i,r){
		REP(j,c){
			if(board[i][j] == '.')continue;
			if(visit[i][j])continue;
			int tmp = DFS0(i,j);
			if(tmp == -1){
				printf("IMPOSSIBLE\n");
				return;
			}
			ret += tmp;
		}
	}
	printf("%d\n", ret);
}

void main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	REP(t,T){
		printf("Case #%d: ", t+1);
		solve();
	}
}
