#include <iostream>
#include <string>

using namespace std;

int t;
string s;
int x[26];

bool f(string s) {
    bool y = true;
    for (int i = 0; i < s.length(); ++i) if (!x[s[i]-'A']--) y = false;
    if (!y) for (int i = 0; i < s.length(); ++i) ++x[s[i]-'A'];
    return y;
}

int main() {
    cin >> t;
    for (int c = 0; c ++< t;) {
        for (int i = 0; i < 26; ++i) x[i] = 0;
        cin >> s;
        for (int i = 0; i < s.length(); ++i) x[s[i]-'A']++;
        int n[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        while (f("ZERO")) ++n[0];
        while (f("TWO")) ++n[2];
        while (f("FOUR")) ++n[4];
        while (f("FIVE")) ++n[5];
        while (f("SEVEN")) ++n[7];
        while (f("EIGHT")) ++n[8];
        while (f("SIX")) ++n[6];
        while (f("NINE")) ++n[9];
        while (f("ONE")) ++n[1];
        while (f("THREE")) ++n[3];
        cout << "Case #" << c << ": ";
        for (int i = 0; i < 10; ++i) for (int j = 0; j < n[i]; ++j) cout << i;
        cout << '\n';
    }
    return 0;
}

