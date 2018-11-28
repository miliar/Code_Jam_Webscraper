#include<iostream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<bitset>
#include<algorithm>
#pragma comment(linker, "/STACK:640000000")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)
using namespace std;
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = 1111;
const int inf = (int)1e9;
int n;
int a[maxn],c[maxn];
void solve() {
	int n; cin >> n;	
	for (int i = 0; i < n; i++) {
		scanf("%d",&a[i]);
	}	
	for (int i = 0; i < n; i++) {
		c[i] = a[i];
	}
	sort(c,c + n);
	for (int i = 0; i < n; i++) {
		a[i] = lower_bound(c,c + n,a[i]) - c;
	}
	int res = 0;
	for (int i = 0; i < n - 1; i++) {
		int pos = -1;
		for (int j = 0; j < n - i; j++) if (a[j] == i) {
			pos = j;
		}
		assert(pos != -1);
		res += min(pos,n - 1 - i - pos);
		while(pos < n - i - 1) {
			swap(a[pos],a[pos + 1]);
			pos++;
		}
	}	
	cout << res << endl;
}
int main() {
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int Cases; cin >> Cases;
	for (int Case = 1; Case <= Cases; Case++) {
		printf("Case #%d: ",Case);
		solve();
	}
	return 0;
}
