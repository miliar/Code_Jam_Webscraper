//Written by technolt~h
 
#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>
 
#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))
 
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()
 
#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << (a[_]) << ' '; cerr << endl;}
#define ll long long
using namespace std;
 
const double PI = 2.0 * acos (0.0);
 
typedef long long LL;
typedef pair <int, int> PII;
 
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

#define maxn

bool calced[10111000];
double f[10111000];

int n;

int bit(int s,int i) {
	return (s>>(i))&1;
}

double calc(int s) {
	if(calced[s]) return f[s];
	
	calced[s]=true;
	
	if(s==(1<<n)-1) f[s]=0;
	else {
		double cur=0;
		f[s]=0;
		REP(i,n) {
			int j=i;
			int d=0;
			while(bit(s,j)) {
				j=(j+1)%n;
				d++;
			}
			cur+=calc(s | (1<<j));
			cur+=n-d;
		}
		f[s]+=cur;
		f[s]/=n;
		
	}
	
	return f[s];
}

int main() {
	freopen("a.inp","r",stdin);
	freopen("a.out","w",stdout);
	int ntest;
	cin >> ntest;
	FOR(test,1,ntest) {
		RESET(calced,false);
		RESET(f,0);
		string s;
		
		cin >> s;
		
		n=s.size();
		
		int state=0;
		REP(i,n)
			if(s[i]=='X') state|=1<<i;
			
		DEBUG(state);
		printf("Case #%d: %.15lf\n",test,calc(state));
	}
}

