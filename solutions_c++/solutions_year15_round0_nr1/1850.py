#include <iostream>
#include <string>

using namespace std;

int getFriends(string levels) {
    int tot = 0;
    int inv = 0;
    int N = levels.size();

    tot = levels[0] - '0';
    for (int i = 1; i < N; i++) {
        int l = levels[i] - '0';
        if (i > tot) {
            inv += (i - tot);
            tot += (i - tot);
        }
        tot += l;
    }

    return inv;
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        int S;
        string levels;
        cin >> S >> levels;

        cout << "Case #" << i << ": " << getFriends(levels) << endl;
    }

    return 0;
}
