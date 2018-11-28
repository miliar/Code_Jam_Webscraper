#include <iostream>
#include <cassert>

using namespace std;

int n, l;
string b;
string g[128];

int main() {
	int tc;
	cin >> tc;
	
	for(int ti = 1; ti <= tc; ++ti) {
		cin >> n >> l;
		for(int i = 0; i < n; ++i) {
			cin >> g[i];
		}
		cin >> b;
		for(char c : b) assert(c == '1');
		
		bool possible = true;
		for(int i = 0; i < n; ++i) {
			if(g[i] == b) possible = false;
		}
		
		cout << "Case #" << ti << ": ";
		if(possible) {
			for(int i = 0; i < l; ++i) {
				cout << "0?";
			}
			cout << " 0";
			for(int i = 0; i < l - 1; ++i) {
				cout << "1";
			}
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << '\n';
	}
	
	return 0;
}
