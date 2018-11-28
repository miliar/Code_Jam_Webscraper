#include <iostream>
#include <string>

using namespace std;

char swap(char c) {
	return c == '+' ? '-' : '+';
}

int main() {
	int t;
	cin >> t;
	
	for (int T = 1; T <= t; T++) {
		string a;
		cin >> a;
		char last = swap(a[0]);
		int res = 0;
		
		for (int i = 0; i < a.length(); i++) {
			if (a[i] != last) res++;
			last = a[i];
		}
		
		cout << "Case #" << T << ": " << res-(last == '+' ? 1 : 0) << "\n";
	}
	
	return 0;
}
