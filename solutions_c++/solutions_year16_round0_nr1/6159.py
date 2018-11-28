#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int number;
        cin >> number;
        if (number == 0) {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }
        else {
            bitset<10> digits;
            digits.set();
            long last = 0;
            while (digits.any()) {
                last += number;
                long temp = last;
                while (temp > 0) {
                    long curr = temp % 10;
                    digits[curr] = 0;
                    temp /= 10;
                }  
            }
            cout << "Case #" << i + 1 << ": " << last << endl;
        }

    }
    return 0;
}