#include <bits/stdc++.h>

using std::cin;

int main() {
    int t;
    std::string s;
    cin >> t;
    for (int ti = 1; ti <= t; ++ti) {
        cin >> s;
        int count = 0;
        for (int i = 1, l = s.length(); i < l; ++i)
            if (s[i] != s[i - 1])
                ++count;
        if (s[s.length() - 1] == '-')
            ++count;
        std::cout << "Case #" << ti << ": " << count << std::endl;
    }
}
