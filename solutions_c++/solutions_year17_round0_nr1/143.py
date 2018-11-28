#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

// one-pass, O(|s|) time, O(k) additional memory
// could use O(k) memory total if k was given before s in the input
void solve() {
	string s;
	int k;
	cin >> s >> k;
	int n = int(s.size());
	// isDiff[j] == 1 means that the flipped state of j-th (mod k) pancake is different from (j-1)-th one
	vector<char> isDiff(k);
	// state is whether the i-th pancake is flipped == xor of isDiff[j] for j<=i
	char state = 0;
	int ans = 0;
	bool impossible = false;
	for (int i = 0; i < n; ++i) {
		state ^= isDiff[i % k];
		if ((isDiff[i % k] = ((s[i] == '-') ^ state))) {
			//E("flip", i);
			++ans;
			state ^= 1;
			if (i + k > n)
				impossible = true;
		}
	}
	if (impossible)
		cout << "IMPOSSIBLE\n";
	else
		cout << ans << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
