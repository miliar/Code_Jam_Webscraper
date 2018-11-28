#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int res = 0;
		string s;
		cin >> s;
		for(int i = 1; i < s.size(); i++) {
			if(s[i] != s[i-1])
				res++;
		}
		if(s.back() == '-')
			res++;
		cout << "Case #" << t << ": " << res << endl;
	}
}
