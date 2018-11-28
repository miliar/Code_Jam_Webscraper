#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>

using namespace std;

bool isPrime(long long num) {
    int count = 0;

    if (num == 1 || num == 2)
        return true;

    if (num % 2 == 0)
        return false;

    for (int i = 2; i <= sqrt(num); i++)
        if (num % i == 0)
            return false;

    return true;
}

void makesDefault(int n, string &num) {
    char *temp;

    temp = new char[n];

    for (int i = 0; i < n; i++) {
        if (i == 0 || i == (n - 1))
            temp[i] = '1';
        else
            temp[i] = '0';
    }

    num = temp;
}

long myPow(int b, int bn) {
    long temp = 1;

    while (bn-- > 0) {
        temp *= b;
    }
    return temp;
}

long baseCal(string a, int b) {
    long total = 0;

    for (int i = 0; i < a.size(); i++) {
        if (a.at(i) == (1 + '0'))
            total += myPow(b, a.size() - 1 - i);
    }

    return total;
}

bool checkAllBase(string start, vector<long> &val) {
    if (start.at(0) != (1 + '0') ||
        start.at(start.length() - 1) != (1 + '0')) {
        return false;
    }

    for (int i = 2; i <= 10; i++) {
        long temp  = baseCal(start, i);
        if (isPrime(temp))
            return false;
        else {
            val.push_back(temp);
        }
    }
}

void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}

char* itoa(int num, char* str, int base)
{
    int i = 0;
    bool isNegative = false;

    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }

    if (num < 0 && base == 10)
    {
        isNegative = true;
        num = -num;
    }

    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }

    if (isNegative)
        str[i++] = '-';

    str[i] = '\0';

    reverse(str, i);

    return str;
}

string makeBaseTwo(long num) {
    char buffer[64] = {0, };

    for (int i = 0; i < 64; i++)
        buffer[i] = 0;

    itoa(num, buffer, 2);
    return string(buffer);
}

string next_num(string s) {
    long temp = 0;

    temp = baseCal(s, 2);
    temp += 1;
    return makeBaseTwo(temp);
}

long getNonTrivial(long val) {
    for (int i = 2; i <= sqrt(val); i++) {
        if (val % i == 0)
            return i;
    }
}

void findValue(string start, int j) {
    vector<long> values;
    int count = 0;

    while (1) {
        if (checkAllBase(start, values)) {
            cout << start;
            for (int i = 0; i < values.size(); i++) {
                cout << " " << getNonTrivial(values.at(i));
            }
            cout << endl;
            count++;
        }

        start = next_num(start);
        values.clear();

        if (count >= j)
            break;
    }
}

int main(void)
{
    int testCase;
    int casenum = 1;

    cin >> testCase;

    while (testCase-- > 0) {
        // start implementation
        int n, j;
        string snum;

        cin >> n >> j;

        makesDefault(n, snum);

        // end

        cout << "Case #" << casenum++ << ": " << endl;
        findValue(snum, j);
        // result
    }

    return 0;
}
