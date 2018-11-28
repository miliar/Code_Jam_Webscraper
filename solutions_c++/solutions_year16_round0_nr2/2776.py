#include <iostream>
#include <bitset>
#include <string>

using namespace std;




int main() {
    int t;
    string  s;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> s;
        // for (uint j = 0; j < s.size(); ++j)
        //     s[j] = (s[j] == '+') ? '1' : '0';
        int count = 0;
        char flag = s[0];
        for (uint j = 0; j < s.size(); ++j) {
            if (flag != s[j]) {
                ++count;
                flag = (flag == '+') ? '-' : '+';
            }
        }

        if (flag == '-')
            ++count;
        cout << "Case #" << i + 1 << ": ";
        cout << count << '\n';
    }
}
