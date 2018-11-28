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
void solve() {
	int n,x; cin >> n >> x;
	multiset<int> st;
	for (int i = 0; i < n; i++) {
		int e; scanf("%d",&e);
		st.insert(e);
	}
	int res = 0;
	while(sz(st) >= 2) {
		res++;
		int mi = *st.begin(); st.erase(st.begin());
		multiset<int>::iterator it = st.upper_bound(x - mi);
		if (it != st.begin()) {
			it--;
			int ma = *it; st.erase(it);
		}
	}
	res += sz(st);
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
