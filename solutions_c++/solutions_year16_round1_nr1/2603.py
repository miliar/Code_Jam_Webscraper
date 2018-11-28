#include <iostream>
#include <string>
#include <set>

using namespace std;

void doit(int casei) {
    string result, s;
    cin >> s;

    result += s[0];

    for (int i = 1; i < s.size(); i++) {
        if (s[i] >= result[0]) {
            result = s[i]+result;
        } else {
            result = result+s[i];
        }
    }

    cout << "Case #" << casei+1 << ": " << result << endl;
}

int main() {
    int cases;
    cin >> cases;
    for (int casei = 0; casei < cases; casei++) {
        doit(casei);
    }
}

