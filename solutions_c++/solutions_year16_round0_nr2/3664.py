#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        string s;
        cin >> s;
        int res = 0;

        while (s.find('-') != string::npos) {
            int pos = int(s.rfind('-'));

            if (s[0] == '+') {
                for_each(s.begin(), s.begin() + s.find('-'), [](char &c) {c = '-';});
                res++;
            }
            for_each(s.begin(), s.begin() + pos + 1, [](char &c) {c = c == '+' ? '-' : '+';});
            reverse(s.begin(), s.begin() + pos + 1);
            res++;
        }
        cout << "Case #" << tst + 1 << ": " << res << "\n";
    }
}
