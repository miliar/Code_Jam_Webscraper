/*
 * =====================================================================================
 *
 *       Filename:  a.cc
 *        Version:  1.0
 *        Created:  2015年05月30日 22时17分40秒
 *       Revision:  none
 *       Compiler:  GNU C++
 *
 *                     I  don't  want  to  be  alone.
 *
 * =====================================================================================
 */
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define PB              push_back
#define SIZE(x)         (int)x.size()
#define clr(x,y)        memset(x,y,sizeof(x))
#define MP(x,y)         make_pair(x,y)
#define RS(n)           scanf ("%s", n)
#define ALL(t)          (t).begin(),(t).end()
#define FOR(i,n,m)      for (int i = n; i <= m; i ++)
#define ROF(i,n,m)      for (int i = n; i >= m; i --)
#define IT              iterator
#define FF              first
#define SS              second

typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long      ull;
typedef vector<int>             vint;
typedef vector<string>          vstring;
typedef pair<int, int>          PII;

void RI (int& x){
	x = 0;
	char c = getchar ();
	while (!(c>='0' && c<='9' || c=='-'))     c = getchar ();
	bool flag = 1;
	if (c == '-'){
		flag = 0;
		c = getchar ();
	}
	while (c >= '0' && c <= '9'){
		x = x * 10 + c - '0';
		c = getchar ();
	}
	if (!flag)      x = -x;
}
void RII (int& x, int& y){RI (x), RI (y);}
void RIII (int& x, int& y, int& z){RI (x), RI (y), RI (z);}
void RC (char& c){
	c = getchar ();
	while (c == ' '||c == '\n')     c = getchar ();
}
char RC (){
	char c = getchar ();
	while (c == ' '||c == '\n')     c = getchar ();
	return c;
}

/**************************************END define***************************************/

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

char a[105][105];
int b[105][105][4];
int n, m;

int solve (){
	clr (b, 0);
	FOR (i, 1, n){
		FOR (j, 1, m){
			if (a[i][j] != '.'){
				b[i][j][0] = 1;
				break;
			}
		}
	}
	FOR (i, 1, n){
		ROF (j, m, 1){
			if (a[i][j] != '.'){
				b[i][j][1] = 1;
				break;
			}
		}
	}
	FOR (j, 1, m){
		FOR (i, 1, n){
			if (a[i][j] != '.'){
				b[i][j][2] = 1;
				break;
			}
		}
	}
	FOR (j, 1, m){
		ROF (i, n, 1){
			if (a[i][j] != '.'){
				b[i][j][3] = 1;
				break;
			}
		}
	}
	int ans = 0;
	FOR (i, 1, n){
		FOR (j, 1, m){
			if (b[i][j][0] && b[i][j][1] && b[i][j][2] && b[i][j][3]){
				return -1;
			}
			if (b[i][j][0] && a[i][j]=='<')	ans ++;
			if (b[i][j][1] && a[i][j]=='>')	ans ++;
			if (b[i][j][2] && a[i][j]=='^')	ans ++;
			if (b[i][j][3] && a[i][j]=='v')	ans ++;
		}
	}
	return ans;
}

int main (){
	int T;
	RI (T);
	FOR (cas, 1, T){
		RII (n, m);
		FOR (i, 1, n){
			FOR (j, 1, m){
				a[i][j] = RC ();

			}
		}
		int ans = solve ();
		printf ("Case #%d: ", cas);
		if (ans == -1){
			puts ("IMPOSSIBLE");
		}else{
			cout << ans << endl;
		}
	}
}


