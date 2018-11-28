#include <bits/stdc++.h>

using namespace std;

int char2int(char c) {
    return c - '0';
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string buffer;
        int N;
        cin >> N;
        cin >> buffer;

        int current_standing = char2int(buffer[0]);
        int needed = 0;
        for (int i = 1; i <= N; i++) {
            if (current_standing < i) {
                needed += i - current_standing;
                current_standing = i;
            }
            current_standing += char2int(buffer[i]);
        }

        cout << "Case #" << t << ": " << needed << endl;
    }

    return 0;
}
