#include <iostream>
#include <vector>
#include <string>

using namespace std;

long long calc(string s) {
    int changes = 1;
    char c = s[0];
    for (int i = 1; i < s.size(); i++) {
        if (c != s[i]) {
            changes++;
            c = s[i];
        }
    }
    if (s.back() == '+') changes--;

    return changes;
}

int main() {
	int testCases;
	string s;
    cin >> testCases;

    for (int i = 1; i <= testCases; i++) {
        cin >> s;
        cout << "Case #" << i << ": ";
        cout << calc(s);
        cout << endl;
    }

    return 0;
}
