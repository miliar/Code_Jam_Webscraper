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
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define ll long long
using namespace std;
 
const double PI = 2.0 * acos (0.0);
 
typedef long long LL;
typedef pair <int, int> PII;
 
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

#define maxn 2111

int n,a[maxn],b[maxn],A[maxn],B[maxn],t[maxn];
bool used[maxn];
bool found;

bool chk(int cur) {
		
		FORD(i,cur,1) {
			B[i]=1;
			FOR(j,i+1,cur) if(t[i]>t[j]) B[i]=max(B[i],B[j]+1);
			if(B[i]>b[i]) return false;			
		}
		return true;
}

void att(int x) {
	if(x>n) {
		FORD(i,n,1) {
			B[i]=1;
			FOR(j,i+1,n) if(t[i]>t[j]) B[i]=max(B[i],B[j]+1);
			if(B[i]!=b[i]) return;
			
		}
		found=true;
		return;
	}
	
	if(t[x]==1) {
		att(x+1);
		return;
	}
	
	FOR(val,1,n) if(!used[val]) {
		used[val]=true;
		
		t[x]=val;A[x]=1;FOR(i,1,x-1) if(t[i]<val) A[x]=max(A[x],A[i]+1);
		
		if(A[x]==a[x] && chk(x)) att(x+1);
		
		used[val]=false;
		
		if(found) return;
	}
}

int main() {
	freopen("a.inp","r",stdin);
	int ntest;cin >> ntest;
	FOR(test,1,ntest) {
		cin >> n;
		FOR(i,1,n) cin >> a[i];
		FOR(i,1,n) cin >> b[i];
		
		
		found=false;
		RESET(used,false);
		RESET(t,0);		
		
		FOR(i,1,n) if(a[i]==1 && b[i]==1) {
			t[i]=1;
			used[1]=true;
			A[i]=1;
			B[i]=1;
		}
		
		att(1);
		
		cout << "Case #" << test << ": ";
		FOR(i,1,n) cout << t[i] << " ";
		cout << endl;
	}
}
	
