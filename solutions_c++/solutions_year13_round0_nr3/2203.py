#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

const int DIGITS_LIMIT = 128;

struct BigNum
{
    int    digits[DIGITS_LIMIT];
    int    size;

    BigNum()
    {
        for (int i = 0; i < DIGITS_LIMIT; ++i)
            this->digits[i] = 0;
        size = 0;
    }
    BigNum(string s)
    {
        reverse(s.begin(), s.end());
        for (int i = 0; i < s.size(); ++i)
            digits[i] = s[i] - '0';
        for (int i = (int)(s.size()); i < DIGITS_LIMIT; ++i)
            digits[i] = 0;
        size = (int)(s.size());
    }
};

void print(const BigNum &a)
{
    cout << "(" << a.size << ")";
    for (int i = a.size - 1; i >= 0; --i)
        cout << a.digits[i];
    cout << endl;
}

bool operator<(const BigNum &a, const BigNum &b)
{
    if (a.size < b.size)
        return true;
    else if (a.size > b.size)
        return false;

    for (int i = a.size - 1; i >= 0; --i)
    {
        if (a.digits[i] > b.digits[i])
            return false;
        else if (a.digits[i] < b.digits[i])
            return true;
    }
    return false;
}

bool operator<=(const BigNum &a, const BigNum &b)
{
    if (a.size < b.size)
        return true;
    else if (a.size > b.size)
        return false;

    for (int i = a.size - 1; i >= 0; --i)
    {
        if (a.digits[i] < b.digits[i])
            return true;
        else if (a.digits[i] > b.digits[i])
            return false;
    }
    return true;
}

bool operator==(const BigNum &a, const BigNum &b)
{
    if (a.size != b.size)
        return false;

    for (int i = a.size - 1; i >= 0; --i)
    {
        if (a.digits[i] != b.digits[i])
            return false;
    }
    return true;
}

BigNum addBigNum(const BigNum &a, const BigNum &b)
{
    BigNum c;
    int i = 0;
    for (i = 0; i < max(a.size, b.size); ++i)
    {
        const int sum = a.digits[i] + b.digits[i] + c.digits[i];
        c.digits[i] = sum % 10;
        c.digits[i + 1] += sum / 10;
    }
    if (c.digits[i] != 0)
        c.size = i + 1;
    else
        c.size = i;

    return c;
}

BigNum multiplyBigNum(const BigNum &a, const BigNum &b)
{
    BigNum c;
    int i = 0, j = 0;
    for (i = 0; i < a.size; i++)
    {
        for (j = 0; j < b.size; j++)
        {
            const int product = a.digits[i] * b.digits[j] + c.digits[j + i];
            c.digits[j + i] = product % 10;
            c.digits[j + i + 1] += product / 10;
        }
    }
    if (c.digits[i - 1 + j - 1 + 1] != 0) // i = a.size, j = b.size.
        c.size = i - 1 + j - 1 + 2;
    else
        c.size = i - 1 + j - 1 + 1;
    return c;
}

BigNum divideBigNumByTwo(const BigNum &a)
{
    BigNum b;
    int carry = 0;
    for (int i = a.size - 1; i >= 0; --i)
    {
        b.digits[i] = (a.digits[i] + carry) / 2;
        carry = (a.digits[i] % 2 == 0? 0 : 10);
    }
    if (b.digits[a.size - 1] == 0)
        b.size = a.size - 1;
    else
        b.size = a.size;
    return b;
}

BigNum &subtractBigNumByOne(BigNum &a)
{
    int i = 0;
    for (i = 0; i < a.size; ++i)
    {
        if (a.digits[i] > 0)
        {
            --a.digits[i];
            break;
        }
        a.digits[i] = 9;
    }
    if (a.digits[a.size - 1] == 0)
        --a.size;
    return a;
}

bool isFair(const BigNum &a)
{
    int right = 0;
    int left = a.size - 1;

    while (right < left)
    {
        if (a.digits[right] != a.digits[left])
            return false;
        ++right;
        --left;
    }
    return true;
}

bool isSquare(const BigNum &a)
{
    if (a.size == 1 
        && a.digits[0] == 1)
        return true;

    BigNum down("1");
    BigNum up(a);

    while (down <= up)
    {
        BigNum mid = divideBigNumByTwo(addBigNum(down, up));
        BigNum square = multiplyBigNum(mid, mid);

        if (square == a)
        {
            if (isFair(mid))
                return true;
            else 
                return false;
        }
        else if (square < a)
            down = addBigNum(mid, BigNum("1"));
        else
            up = subtractBigNumByOne(mid);
    }
    return false;
}

int main ()
{
    int T;
    int caseCount = 0;
    cin >> T;
    while ( T-- )
    {
        caseCount++;
        string As, Bs;
        cin >> As >> Bs;
        const BigNum A(As), B(Bs);

        int number = 0;
        for (BigNum i = A; i <= B; i = addBigNum(i, BigNum("1")))
        {
            if (isFair(i) 
                && isSquare(i))
                ++number;
        }

        cout << "Case #"
             << caseCount
             << ": "
             << number;
        
        cout << endl;
    }
    return 0;
}