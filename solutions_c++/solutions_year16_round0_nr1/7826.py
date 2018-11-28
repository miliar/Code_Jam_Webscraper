#include <iostream>

using namespace std;
int main(int argc, char** argv)
{
    bool digits[10];
    int T, N;
    int d, count, tmpN, initN;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> initN;
        if (initN == 0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }

        for (int j = 0; j < 10; ++j)
            digits[j] = false;

        count = 0;
        N = 0;
        while (count < 10) {
            N += initN;
            tmpN = N;
            do {
                d = tmpN % 10;
                if (!digits[d]) {
                    digits[d] = true;
                    ++count;
                }
            } while (tmpN = tmpN / 10);
        }
        cout << "Case #" << i << ": " << N << endl;
    }
}
