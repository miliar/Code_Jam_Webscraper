#include <iostream>
#include <vector>
using namespace std;

int main () {
    int N;
    cin >> N;
    int cnt = 1;
    while (cnt <= N) {
        int S;
        char c;
        cin >> S;
        int ask = 0, stand = 0;
        for (int i = 0; i <= S; ++i) {
            cin >> c;
            int d = c - '0';
            if (stand >= i) {
                stand += d;
            }
            else {
                ask += (i - stand);
                stand = i + d;
            }
        }
        cout << "Case #" << cnt << ": " << ask << endl;
        ++cnt;
    }
    return 0;
}