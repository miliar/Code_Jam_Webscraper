#include <iostream>
using namespace std;

int main() {
    int T, N;
    cin >> T;
    for (int t=1; t<=T; t++) {
        cin >> N;
        cout << "Case #" << t << ": ";
        if (N == 0)
            cout << "INSOMNIA\n";
        else {
            // seen & (1 << digit) = 1 iff digit already seen
            long long int k, digit, i = 1, seen = 0;
            while (seen < 1023) {
                k = i*N;
                while (k>0) {
                    digit = k % 10;
                    if ((seen & (1 << digit)) == 0)
                        seen += (1 << digit);
                    k = (k-digit)/10;
                }
                i++;
            }
            cout << ((i-1)*N) << "\n";
        }
    }
}
