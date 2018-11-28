#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:300000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int n,x,s[10000];

void read(){
	scanf("%d%d", &n, &x);
	forn(i,n)
		scanf("%d", &s[i]);
}

bool ok(int c){
	int l = 0, r = n-1;
	while (r>l){
		if (s[r]+s[l] <= x){
			r--;
			l++;
		}else{
			r--;
		}
		c--;
	}
	if (r == l)
		c--;
	return c >= 0;
}

void solve(){
	sort(s, s+n);
	int lf = 0, rg = n;
	while (rg-lf>1){
		int m = (lf+rg)/2;
		if (ok(m))
			rg = m;
		else
			lf = m;
	}
	for (int i=lf; i<=rg; i++)
		if (ok(i)){
			printf("%d\n", i);
			return;
		}
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++){
		read();
		printf("Case #%d: ", test);
		solve();
	}
    return 0;
}