#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int checkDigit(long long value, bool *check) {
    int count = 0;
    while (value > 0) {
        int temp = value % 10;
        check[temp] = true;
        value /= 10;
    }

    for (int i = 0; i < 10; i++)
        if (check[i] == true)
            count++;

    return count;
}

int main(void)
{
    int testCase;
    int casenum = 1;

    cin >> testCase;

    while (testCase-- > 0) {
        // start implementation
        long long start = 0;
        bool check[10] = {0, };
        int count = 0;
        int index = 1;
        int sameCount = 0;
        int number = 0;

        for (int i = 0; i < 10; i++)
            check[i] = false;

        cin >> start;
        number = start;

        while (count < 10) {
            int temp;
            count = checkDigit(number, check);

            if (sameCount > 5 || count >= 10) {
                break;
            }

            temp = number;
            number = start * (++index);

            if (temp == number)
                sameCount++;
        }

        // end

        cout << "Case #" << casenum++ << ": ";
        if (count < 10)
            cout << "INSOMNIA" << endl;
        else
            cout << number << endl;
        // result
    }

    return 0;
}
