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
int m,n;
string s[8];
int nxt[111][26],last;
int w[8];
void add(int id) {
	int v = 0;
	for (int i = 0; i < sz(s[id]); i++) {
		int g = s[id][i] - 'A';
		if (nxt[v][g] == -1) {
			nxt[v][g] = last++;
		}
		v = nxt[v][g];
	}
}
int calc() {
	int cur = 0;
	for (int i = 0; i < n; i++) {
		memset(nxt,-1,sizeof(nxt));
		last = 1;
		bool was = false;
		for (int j = 0; j < m; j++) if (w[j] == i) {
			was = true;
			add(j);
		}
		if (was) cur += last;
	}
	return cur;
}
void solve() {
	cin >> m >> n;
	for (int i = 0; i < m; i++) {
		cin >> s[i];
	}
	int st = 1;
	for (int i = 0; i < m; i++) {
		st *= n;
	}
	int ma = 0;
	int cnt = 0;
	for (int mask = 0; mask < st; mask++) {
		int mmask = mask;
		for (int i = 0; i < m; i++) {
			w[i] = mmask % n;
			mmask /= n;
		}
		int cur = calc();
		if (cur > ma) {
			ma = cur;
			cnt = 1;
		} else if (cur == ma) {
			cnt++;
		}
	}
	cout << ma << " " << cnt << endl;
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
