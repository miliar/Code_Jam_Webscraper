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

int n;
vector <double> pl[2];

void read(){
	cin >> n;
	forn(it,2){
		pl[it].resize(n);
		forn(i,n)
			cin >> pl[it][i];
		sort(all(pl[it]));
	}
}

void solve(){
	int dw = 0, w = 0, j = 0, sm = 0, mid = 0;
	for (int i=0; i<n; i++){
		while (j < n && pl[1][j] < pl[0][i]){
			j++;
		}
		if (j!=n)j++;
		else w++;
	}
	for (int t=1; t<=n; t++){
		bool ok = true;
		for (int i=0; i<t; i++){
			ok = ok && (pl[1][i] < pl[0][n-t+i]);
		}
		if (ok) dw = t;
	}
	cout << dw << ' ' << w << endl;
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	for (int cs=1; cs<=t; cs++){
		read();
		cout << "Case #" << cs << ": ";
		solve();
	}
    return 0;
}