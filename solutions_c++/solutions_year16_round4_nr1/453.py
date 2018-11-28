#include <bits/stdc++.h>

using namespace std;

string foo(char w, int n) {
	if(n == 0)
		return string("") + w;
	string s1, s2;
	switch(w) {
	case 'P':
		s1 = foo('P', n - 1);
		s2 = foo('R', n - 1);
		break;
	case 'R':
		s1 = foo('R', n - 1);
		s2 = foo('S', n - 1);
		break;
	case 'S':
		s1 = foo('S', n - 1);
		s2 = foo('P', n - 1);
		break;
	}
	if(s1 > s2)
		swap(s1, s2);
	return (s1 + s2);
}

void solve(int t) {
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	printf("Case #%d: ", t);
	auto check = [&](string & s) {
		return count(s.begin(), s.end(), 'P') == P && count(s.begin(), s.end(), 'R') == R && count(s.begin(), s.end(), 'S') == S;
	};
	string ans;
	string s = foo('P', N);
	//cout << s << '\n';
	if(check(s) && (ans.empty() || s < ans))
		ans = s;
	s = foo('R', N);
	//cout << s << '\n';
	if(check(s) && (ans.empty() || s < ans))
		ans = s;
	s = foo('S', N);
	//cout << s << '\n';
	if(check(s) && (ans.empty() || s < ans))
		ans = s;
	if(ans.empty()) cout << "IMPOSSIBLE";
	else cout << ans;
	cout << '\n';
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
		solve(t);
}
