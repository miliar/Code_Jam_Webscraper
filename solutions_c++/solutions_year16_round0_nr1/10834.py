#include <iostream>

void numbers(int num);

using namespace std;

int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int main() {
    int testCases = 0, start = 0;
    cin >> testCases;
    for (int i = 1; i <= testCases; ++i) {
        cin >> start;

        cout << "Case #" << i << ": ";
        if (start == 0) {
            cout << "INSOMNIA\n";
        } else {
            for (int j = 0; j < 10; ++j) {
                digits[j] = 0;
            }
            numbers(start);
        }


    }

    return 0;
}


void numbers(int numder) {
    int digit = 0, counter = 0, i = 0, num = 0;
    while (++i) {

        num = numder * i;

        while (num > 0) {
            digit = num % 10;

            num -= digit;
            if (digits[digit] == 0) {
                digits[digit] = 1;
                counter++;
            }
            num /= 10;
        }

        if (counter == 10) {
            cout << numder * i<<"\n";
            break;
        }

    }
}