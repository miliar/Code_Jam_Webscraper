#include <iostream>
using namespace std;

int main() {

    long T;
    char s[101];
    char SET[2] = {'-', '+'};
    cin >> T;
    for (long i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        cin >> s;

        long len;
        for (len = 0; s[len]; ++len);

        long count = 0;
        for (long j = len - 1, type = 0; j >= 0; --j) {
            if (s[j] == SET[type]) {
                type ^= 1;
                count++;
            }
        }
        cout << count << "\n";
    }
}
