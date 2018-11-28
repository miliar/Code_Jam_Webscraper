#include <iostream>
#include <unordered_set>

using namespace std;

int count_sheep(int start) {
    int number, quotient, remainder;
    unordered_set<int> myset;

    for (int i = 1; ; i++) {
        number = i * start;
        quotient = number;
        while (quotient) {
            remainder = quotient % 10;
            quotient = quotient / 10;
            myset.insert(remainder);
            if (myset.size() == 10) {
                return number;
            }
        }
    }
}

int main() {
    int t, x;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> x;
        if (x) 
            cout << "Case #" << i << ": " << count_sheep(x) << endl;
        else
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
}
