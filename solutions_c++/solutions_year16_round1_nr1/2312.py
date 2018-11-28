#include <cstdio>
#include <iostream>
#include <string>
#include <queue>
#include <cmath>
using namespace std;

string sol(string s) {
	int i;
	string r = "";
	r += s[0];
	for (i = 1; i < s.size(); i++) {
		if (s[i] >= r[0]) {
			r.insert(0, 1, s[i]);
		} else {
			r += s[i];
		}
	}
	return r;
}

int main() {
	int T, S;
    int i;
    scanf("%d", &T);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (i = 1; i <= T; i++) {
    	string s;
    	cin >> s;
    	printf("Case #%d: %s\n", i, sol(s).c_str());
    }
}