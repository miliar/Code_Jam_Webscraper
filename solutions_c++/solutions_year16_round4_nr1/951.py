#include <iostream>
#include <algorithm>
using namespace std;

static char winner(char a, char b) {
	if(a == 'R' && b == 'P') return b;
	if(a == 'P' && b == 'S') return b;
	if(a == 'S' && b == 'R') return b;
	if(b == 'R' && a == 'P') return a;
	if(b == 'P' && a == 'S') return a;
	if(b == 'S' && a == 'R') return a;
	return a;
}

static bool ok(string s, int len) {
	int inc = 1;
    while(inc < len) {
		for(int i = 0; i < len; i += inc + inc) {
			const int j = i + inc;
			if(s[i] == s[j]) return false;
			s[i] = winner(s[i], s[j]);
		}
		inc *= 2;
	}
	return true;
}

int main() {
  int T;
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) {
cerr << cn << " of " << T << '\n';

    int N, R, P, S;
	cin >> N >> R >> P >> S;

	string s;
	s += string(R, 'R');
	s += string(P, 'P');
	s += string(S, 'S');

	sort(begin(s), end(s));
	string ans = "IMPOSSIBLE";
	do {
		if(ok(s, (int)s.size())) {
			ans = s;
			break;
		}
	} while(next_permutation(begin(s), end(s)));

	cout << "Case #" << cn << ": ";
	cout << ans << '\n';
  }
}
