#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long int64;

int64 bin_to_base(int64 num, int base)
{
    int64 result = 0;

    int n = 0;
    while (num > 0)
    {
        result += (num & 1) * (pow(base, n));
        num >>= 1;
        n++;
    }

    return result;
}

/*
int64 dec_to_bin(int64 num)
{
    int64 result = 0;


    while (num > 0)
    {
        if (num & 1) {
            result++;
        }

        result *= 10;
        num >>= 1;
    }

    return  result;
}
 */

int64 find_divisor(int64 num)
{
    double n = sqrt(num) + 1;

    for (int64 i = 2; i < n; ++i)
    {
        if (num % i == 0)
            return i;
    }

    return -1;

}

int main()
{
    int t;

    cin >> t;

    int N, J;
    cin >> N >> J;

    cout << "Case #1: " << endl;

    int64 ten_num[12];

    ten_num[2] = (1 << (N - 1)) + 1;

    for (int base = 3; base <= 10; ++base)
        ten_num[base] = bin_to_base(ten_num[2], base);


    vector<int64> divisors;
    divisors.reserve(9);

    while (J) {

        for (int base = 2; base <= 10; ++base) {

            int64 divisor = find_divisor(ten_num[base]);
            if (divisor != -1)
            {
                divisors.push_back(divisor);
            }
            else
            {
                break;
            }
        }

        if (divisors.size() == 9)
        {
            cout << ten_num[10] << " ";
            for (auto d : divisors)
                cout << d << " ";
            cout << endl;
            J--;
        }
        else
        {
            /* next case */
            ten_num[2] += 2;

            for (int base = 3; base <= 10; ++base)
                ten_num[base] = bin_to_base(ten_num[2], base);

            divisors.clear();
        }
    }

    return 0;
}