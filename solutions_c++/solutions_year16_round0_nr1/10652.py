#include <iostream>

using namespace std;

int main()
{
    int t;


    cin >> t;
    for (int i = 0; i < t; i++) {
        int inNumber;
        bool existDigit[10];

        cout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < 10; j++) {
            existDigit[j] = false;
        }

        cin >> inNumber;

        if (inNumber != 0) {
            bool sleep = false;
            int number;
            int digit;

            int j = 1;
            while (!sleep) {
                int tempNumber;
                number = inNumber * j;
                tempNumber = number;

                while (tempNumber != 0) {
                    digit = tempNumber % 10;
                    existDigit[digit] = true;
                    tempNumber /= 10;
                }

                sleep = true;
                for (int k = 0; k < 10; k++) {
                    if (!existDigit[k]) {
                        sleep = false;
                        break;
                    }
                }

                j++;
            }

            cout << number <<endl;
        } else {
            cout << "INSOMNIA" <<endl;
        }
    }

    return 0;
}
