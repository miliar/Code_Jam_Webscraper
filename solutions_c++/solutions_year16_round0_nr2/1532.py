#include <iostream>
using namespace std;
string s;
int doit() {
    char c = s[0];
    int res = 0;
    for (int i = 1; i < s.length(); ++i) {
	if (s[i] != c) {
	    c = s[i];
	    ++res;
	}
    }
    if (s[s.length() - 1] == '-') ++res;
    return res;
}
int T;
int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
	cin >> s;
	printf("Case #%d: %d\n", t, doit());
    }
    return 0;
}
