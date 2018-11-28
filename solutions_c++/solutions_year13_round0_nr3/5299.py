#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;

bool isPalindrome(int num)
{
    // cout << "---------------------" << endl;
    // cout << "num = " << num << endl;
    int bitNum = (int) log10(num);
    bool result = false;
    // if (bitNum == 0)
    // {
    //     return true;
    // }
    int n[bitNum + 1];
    bzero(n, sizeof(int) * (bitNum + 1));
    
    for (int i = 0; i < (bitNum + 1); ++i)
    {
        n[i] = num % 10;
        num /= 10;
        // cout << "n[bitNum] = " << n[i] << endl;
    }
    for (int j = 0; j < ((bitNum + 1) / 2 + 1); ++j)
    {
// cout << "n[" << j << "] = " << n[j] << " n[" << (bitNum - 1) << "] = " << n[bitNum - j] << endl;
        if (n[j] == n[bitNum - j])
        {
            
            result = true;
        } else {
            result = false;
            break;
        }
    }
    // cout << "---------------------" << endl;
    return result;
}

bool isSquare(int num)
{
    // if (num == ((int)sqrt(num)) * ((int)sqrt(num)))
    // {
    //     cout << "num = " << num << "squre" << endl;
    // }
    return num == ((int)sqrt(num)) * ((int)sqrt(num));
}

int calculate(int min, int max)
{
    int count = 0;
    for (int i = min; i <= max; ++i)
    {
        if (isPalindrome(i) && isSquare(i) && (isPalindrome((int)sqrt(i))))
        {
            // cout << "i = " << i << endl;
            count++;
        }
    }
    return count;
}

int main(int argc, char const *argv[])
{
    int t, a, b;
    t = a = b = 0;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> a, cin >> b;
        int result = calculate(a, b);
        cout << "Case #" << (i + 1) << ": " << result << endl;
    }
    return 0;
}
