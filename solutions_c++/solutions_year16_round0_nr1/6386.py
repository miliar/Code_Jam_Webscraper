#include <iostream>
#include <string>
#include <vector>
using namespace std;

void extractDigits(vector<int> &digits, int &count, int value) {
    int digit = 0;
    while(value) {
        digit = value % 10;
        if(digits[digit] == 0) {
            digits[digit] = 1;
            ++count;
        }
        value /= 10;
    }
}

int main() {
    int t = 0;
    int n = 0;

    cin >> t;

    for(int i = 0; i < t; ++i) {
        vector<int> v(10);
        int count = 0;
        cin >> n;
        if(n == 0) {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }

        int j = 1;
        int val = n;

        while(true) {
            extractDigits(v, count, val);
            if(count == 10) {
                break;
            }
            val = n * j++;
        }
        cout << "Case #" << i + 1 << ": " << val << endl;
    }

    return 0;
}
