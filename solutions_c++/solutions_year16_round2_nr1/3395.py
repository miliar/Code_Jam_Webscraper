#include <bits/stdc++.h>
using namespace std;
#define e1 first
#define e2 second
#define pb push_back
#define mp make_pair
#define boost ios_base::sync_with_stdio(false)
#define eb emplace_back
#define OUT(x) {cout << x; exit(0); }
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> PII;
typedef pair <ll, ll> PLL;
typedef pair <PLL, PLL> PP;
typedef unsigned int ui;
const int mod = 1e9+7;
const int inf = 1e9+9;
const ll MOD = 1e9+696969;
const ll INF = 1e18;
#define maxn 1000100
int n, m, a, b, c, jest, ocz, zap, it;
int ile[190];
int t[15];

inline void perform(int num, string N) {
	if (num == 0) {
		t[num] = ile['Z'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	
	if (num == 2) {
		t[num] = ile['W'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 3) {
		t[num] = ile['R'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 4) {
		t[num] = ile['U'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 5) {
			t[num] = ile['F'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 6) {
			t[num] = ile['X'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 7) {
			t[num] = ile['S'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 8) {
			t[num] = ile['H'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 9) {
		t[num] = ile['I'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
	if (num == 1) {
		t[num] = ile['O'];
		for (int i=0; i<N.size(); ++i)
		  ile[N[i]]-=t[num];
	}
}

int main() {
	scanf("%d", &n);
	for (int z=1; z<=n; ++z) {
		string s = "";
		cin >> s;
		for (int i=0; i<26; ++i) ile[i + 'A'] = 0;
		for (int i=0; i<10; ++i) t[i] = 0;
		for (int i=0; i<s.size(); ++i) ile[s[i]]++;
		printf("Case #%d: ", z);
		perform(0, "ZERO");
		perform(2, "TWO");
		perform(4, "FOUR");
		perform(3, "THREE");
		perform(6, "SIX");
		perform(8, "EIGHT");
		perform(7, "SEVEN");
		perform(5, "FIVE");
		perform(9, "NINE");
		perform(1, "ONE");
		for (int i=0; i<10; ++i)
		  for (int j=1; j<=t[i]; ++j) printf("%d", i);
		printf("\n");
	}
}
