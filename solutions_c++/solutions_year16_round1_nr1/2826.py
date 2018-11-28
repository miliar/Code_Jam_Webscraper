#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        string s;
        cin >> s;
        string res;

        for (auto c: s) {
            auto pos = res.find_first_not_of(c);

            if (pos == string::npos || res[pos] < c) {
                res = c + res;
            } else {
                res += c;
            }
        }
        cout << "Case #" << tst + 1 << ": " << res << '\n';
    }
}
