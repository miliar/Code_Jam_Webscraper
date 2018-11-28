#include <iostream>
#include <stdlib.h>
using namespace std;

int checkNumber(int number)
{
    int mul_check,ans, allNum[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, multi = 1, count = 1, digit;
    while (count != 11) {
        ans = multi * number;
        //cout <<multi << " * " <<number << " = "<< ans << endl;
        mul_check = ans;
        while (mul_check > 0) {
            digit = mul_check % 10;
            for (int i = 0; i < 10; i++) {
                if (digit == allNum[i]) {
                    allNum[i] = 10;
                    count++;
                    break;
                }
            }
            mul_check /= 10;
        }
        multi++;

    }
    // for (int i = 0; i < 10; i++)
    //     {
    //         cout << allNum[i] << " " ;
    //     }
    //     cout << endl;
    return ans;
}

void printNumber(int ans[], int n)
{
    for (int i = 0; i < n; i++) {
        if (ans[i] == -1) {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;

        } else {
            cout << "Case #" << i + 1 << ": " << ans[i] << endl;
        }
    }
}

int main()
{
    int t, number, x, p = 0;
    cin >> t;
    int ans[t];
    for (int i = 0; i < t; i++) {
        cin >> number;
        if (number != 0)
        {
            number = abs(number);
            x = checkNumber(number);
        }else{
            x = -1;
        }
        ans[p] = x;
        p++;
    }
    printNumber(ans, t);

    return 0;
}