#include <iostream>

using namespace std;

int main() {
    int T, N;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        if (N == 0) {
            cout << "Case #" << i+1 << ": INSOMNIA\n";
        } else {
            int temp = 0;
            int arr = 0x3FF;
            do {
                temp += N;
                int tens = temp;
                while (tens) {
                    int mask = 0x3FF;
                    int rem = tens % 10;
                    tens /= 10;
                    mask ^= 1 << rem;
                    arr &= mask;
                }
            } while (arr);
            cout << "Case #" << i+1 << ": " << temp << "\n";
        }
    }
}
