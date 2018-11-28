#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int R, C, W, answer;
        cin >> R >> C >> W;
        answer = C / W * R + !!(C % W) + W - 1;
        cout << "Case #" << t << ": " << answer << endl;
    }
}
