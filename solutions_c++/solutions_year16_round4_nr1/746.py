/*************************************************************************

       Author:            palayutm
       Created Time :     Sat 28 May 2016 09:55:21 PM CST

       File Name:         a.cc
       Description:       new style, new life

 ************************************************************************/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

string dfs (char now, int d){
	if (d == 0){
		string s;
		s += now;
		return s;
	}
	string x, y;
	if (now == 'P'){
		x = dfs('P', d-1);
		y = dfs('R', d-1);
	}
	if (now == 'R'){
		x = dfs('R', d-1);
		y = dfs('S', d-1);
	}
	if (now == 'S'){
		x = dfs('P', d-1);
		y = dfs('S', d-1);
	}
	return min(x+y, y+x);
}

bool check (string s, int a, int b, int c){
	FOR (i, 0, SIZE (s)-1){
		if (s[i] == 'R'){
			a --;
		}else if (s[i] == 'P'){
			b --;
		}else{
			c --;
		}
	}
	return a == 0 && b == 0 && c == 0;
}

int main (){
	int T;
	cin >> T;
	FOR (cas, 1, T){
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		string x[3] = {dfs('P', N), dfs('R', N), dfs('S', N)};
		string ans = "";
		FOR (i, 0, 2){
			if (check(x[i], R, P, S)){
				if (ans == ""){
					ans = x[i];
				}else{
					ans = min(ans, x[i]);
				}
			}
		}
		printf ("Case #%d: ", cas);
		if (ans == ""){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << ans << endl;
		}
	}
}

