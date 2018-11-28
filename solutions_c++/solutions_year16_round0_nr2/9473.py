#include <iostream>
#include <string>
using namespace std;

int revert(string s) {
    if(s.empty()) return 0;
    char cur = s[0];
    int cnt = 0;
    for(int i = 0; i < (int)s.size(); ++i) {
	if(cur != s[i]) {
	    cnt++;
	    cur = s[i];
	}
    }
    return cur == '-' ? cnt + 1 : cnt;
}

int main() {
    int T;
    string s;
    cin >> T;

    for(int i = 1; i <= T; ++i) {
	cin >> s;
	cout << "Case #" << i << ": " << revert(s) << "\n";
    }
}
