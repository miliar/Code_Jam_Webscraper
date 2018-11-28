#include <bits/stdc++.h>

using namespace std;

#define fr(a, b, c) for(int a = b; a < c; a++)

#define dbg(x) cerr << ">>> " << x << endl;
#define _ << ", " <<

typedef long long ll;

int main() {
	ios_base::sync_with_stdio(false);

	int T;
	
	cin >> T;
	
	fr(cas, 1, T+1) {
		string s;
		cin >> s;
		
		int ans = 0;
		
		while(!s.empty() && s.back() == '+') s.pop_back();
	
		fr(i, 1, s.size()) {
			if(s[i] != s[i-1]) ans++;
		}	
	
		printf("Case #%d: %d\n", cas, ans + (s.empty() ? 0 : 1));
	}

	return 0;
}
