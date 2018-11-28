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

int f[2][4][4];
int row[2];

void read(){
	forn(it,2){
		scanf("%d", &row[it]);
		row[it]--;
		forn(i,4){
			forn(j,4){
				scanf("%d", &f[it][i][j]);
			}
		}
	}
}

void solve(){
	set <int> res[2];
	forn(it,2){
		forn(j,4)
			res[it].insert(f[it][row[it]][j]);
	}
	vector <int> ans;
	for (set <int> :: iterator it = res[0].begin(); it!=res[0].end(); it++){
		if (res[1].count(*it))
			ans.pb(*it);
	}
	if (sz(ans) == 0)
		puts("Volunteer cheated!");
	if (sz(ans) == 1)
		printf("%d\n", ans[0]);
	if (sz(ans) > 1)
		puts("Bad magician!");
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; cs++){
		read();
		printf("Case #%d: ", cs);
		solve();
	}
    return 0;
}