#include <iostream>
#include <string>

using namespace std;

int solve(int m, string s) {
    int stood = 0;
    int frien = 0;

    for (int shy = 0; shy < s.size(); ++shy) {
        int cnt = s[shy] - '0';

        int need_stood = shy;

        if (stood >= m) {
            return frien;
        }

        if (need_stood <= stood) {
            stood += cnt;
        }
        else {
            frien++;
            stood += (1 + cnt);
        }
    }

    return frien;
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        int m;
        string s;

        cin >> m >> s;

        printf("Case #%d: %d\n", i, solve(m, s));
    }
    return 0;
}
