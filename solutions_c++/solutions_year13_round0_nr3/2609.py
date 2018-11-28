#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <string>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <cmath>

using namespace std;

string convert_int(long long num)
{
    stringstream ss;
    ss << num;
    return ss.str();
}

bool is_palindrome(long long num)
{
    string str = convert_int(num);
    int len = str.length();
    bool ret = true;

    for (int i = 0; i < len; i++) {
        if (str[i] != str[len - 1 - i]) {
            ret = false;
            break;
        }
    }

    return ret;
}

bool is_square(long double num)
{
    double num2 = sqrt(num);
    bool ret = true;

    if (num2 != round(num2)) {
        ret = false;
        goto DONE;
    }

    ret = is_palindrome(num2);

DONE:
    return ret; 
}

int main()
{
    int T;
    long long A, B;
    int count;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        count = 0;
        cin >> A >> B;

        for (long long j = A; j <= B; j++) {
            if (is_palindrome(j) && is_square(j)) {
                count++;
            }
        }

        cout << "Case #" << i << ": " << count << endl;
    }
}
