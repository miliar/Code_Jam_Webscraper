/*
 * =====================================================================================
 *
 *       Filename:  b.cc
 *        Version:  1.0
 *        Created:  2015年05月30日 22时41分27秒
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

pair<double, double> a[105];
int n;
double V, X;

double cal1 (double t){
	double v = V;
	double avg = 0.0;
	FOR (i, 1, n){
		double tv = t*a[i].SS;
		if (tv >= v){
			tv = v;
		}
		avg += tv * a[i].FF;
		v -= tv;
	}
	return avg/V;
}

double cal2 (double t){
	double v = V;
	double avg = 0.0;
	ROF (i, n, 1){
		double tv = t*a[i].SS;
		if (tv >= v){
			tv = v;
		}
		avg += tv * a[i].FF;
		v -= tv;
	}
	return avg/V;
}

int main (){
	int T;
	RI (T);
	FOR (cas, 1, T){
		cin >> n >> V >> X;
		FOR (i, 1, n){
			cin >> a[i].SS >> a[i].FF;
		}
		sort (a+1, a+n+1, greater<pair<double, double> >());
		printf ("Case #%d: ", cas);
		if (a[1].FF < X || a[n].FF > X)	puts ("IMPOSSIBLE");
		else{
			double low = 0, high = 1e18;
			while (high - low > 1e-9){
				double mid = (low + high)/2.0;
				//cout << cal1 (mid) << " " << cal2 (mid)<< endl;
				if (cal1 (mid)>=X && cal2 (mid)<=X){
					high = mid;
				}else{
					low = mid;
				}
			}
			printf ("%.10f\n", high);
		}
	}
}


