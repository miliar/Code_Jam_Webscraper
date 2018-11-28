#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	
	int kase = 1;
	int t;
	cin >> t;
	while(t--) {
		string in;
		cin >> in;
		string s;
		for(auto &each : in) {
			if(s.empty()) {
				s += each;
			}
			else {
				if(s.back() != each) {
					s += each;
				}
			}
		}
		if(s.back() == '+') {
			s.pop_back();
		}
		cout << "Case #" << kase++ << ": ";
		cout << s.size() << '\n';
	}

	return 0;
}
