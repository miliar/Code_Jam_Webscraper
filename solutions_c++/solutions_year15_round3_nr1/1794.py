#include <iostream>

using namespace std;

int main () {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int R, C, W;
        cin >> R >> C >> W;
        cout << "Case #" << i << ": " << (C-1)/W + W << endl;
    }
    return 0;
}
