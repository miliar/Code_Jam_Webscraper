#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int tests;

int main() {
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        string str;
        cin >> str;

        int sol = 0;
        int curr = str.size() - 1;
        while (curr >= 0) {
            if (str[curr] == '+') {
                curr--;
                continue;
            } else if (str[0] == '+') {
                int cplus = 0;
                while (str[cplus] == '+') cplus++;
                reverse(str.begin(), str.begin() + cplus);
                for (int i = 0; i < cplus; ++i)
                    str[i] = str[i] == '-' ? '+' : '-';
                sol++;
            }

            reverse(str.begin(), str.begin() + curr + 1);
            for (int i = 0; i <= curr; ++i) str[i] = str[i] == '-' ? '+' : '-';
            sol++;
        }

        cout << "Case #" << t << ": " <<  sol << endl;
    }

    return 0;
}