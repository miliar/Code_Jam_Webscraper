#include <iostream>
#include <cstdlib>
#include <stdint.h>

using namespace std;

bool test_digits(bool* array) {
    return !(array[0] && array[1] && array[2] && array[3] && array[4] && array[5]
            && array[6] && array[7] && array[8] && array[9]);
}

void solution(int i) {
    bool digits[10] = {false};
    int start_digit = 0;
    cin >> start_digit;

    if (start_digit == 0) {
        cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        return;
    }

    uint64_t result = 0;
    uint64_t buffer = 0;
    while(test_digits(digits)) {
        result += start_digit;
        buffer = result;

        while (buffer != 0) {
            digits[buffer % 10] = true;
            buffer /= 10;
        }
    }

    cout << "Case #" << i+1 << ": " << result << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        solution(i);
    }
    return 0;
}
