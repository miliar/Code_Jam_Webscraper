#include <iostream>

using namespace std;

void doit() {
    int Smax;
    cin >> Smax;
    int tot = 0;
    int ans = 0;
    for (int S = 0; S <= Smax; ++S) {
        char Sic;
        cin >> Sic;
        int Si = Sic - '0';
        if (Si == 0 && tot == 0) {
            ans += 1;
        } else if (Si == 0) {
            tot -= 1;
        } else {
            tot += Si - 1;
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) { cout << "Case #" << i << ": "; doit(); }
    return 0;
}
