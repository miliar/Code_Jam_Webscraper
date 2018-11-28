#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

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
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
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


int main(){
#ifdef gridnevvvit
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int T;
	scanf("%d", &T);
	int pos = 1;
	while (T--) {
		int n, m;
		scanf("%d %d", &n, &m);
		vector < pair<int,int> > d;
		int must = 0;
		printf("Case #%d: ", pos);
		forn(i,m) {
			int a, b, p;
			scanf("%d %d %d", &a, &b, &p);
			while (p--) {
				d.push_back(mp(a,b));
				must += (b - a) * (n + (n - (b - a) + 1)) / 2;
			}
		}
		sort(all(d));
		int answer = 0;
		multiset < int > opens;
		for(int i = 1; i <= n; i++) {
			forn(j,sz(d)) if (d[j].first == i) opens.insert(i);
			forn(j,sz(d)) if (d[j].second == i) {
				multiset < int > ::iterator it = opens.end();
				it--;
				int val = *it;
				answer += (i - val) * (n + n - (i - val) + 1)/2;
				opens.erase(it);
			}
		}
		pos++;
		cout << must - answer << endl;
	}
	return 0;
}