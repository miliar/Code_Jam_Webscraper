#include <iostream>
using namespace std;

char s[1005];
int charToInt(char c) { return c-'0'; }

int main() {
    int T, n;
    int level;

    cin >> T;
    for (int t = 1; t <= T; t++) {
        int standed = 0, invite = 0;

        cin >> n >> s;

        for (level = 0; level <= n; level++) {
            int si = charToInt(s[level]);
            if (si > 0 && standed < level) {
                invite += (level - standed);
                standed = level;
            }
            standed += si;
            if (standed >= n) break;
        }

        cout << "Case #" << t << ": " << invite << endl;
    }


    return 0;
}
