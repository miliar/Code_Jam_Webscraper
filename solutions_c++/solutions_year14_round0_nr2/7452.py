#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>

#define NDEBUG

const long double EPSILON = 0.000000001;

struct real
{
    real(long double val) : val(val) {}
    operator long double() { return val; }
    long double val;
};

int compare(const real &r1, const real &r2)
{
    if (fabs(r1.val - r2.val) <= EPSILON)
        return 0;

    return r1.val - r2.val < 0 ? -1 : 1;
}

bool operator==(const real &r1, const real &r2)
{ return compare(r1, r2) == 0; }

bool operator<(const real &r1, const real &r2)
{ return compare(r1, r2) == -1; }

bool operator>(const real &r1, const real &r2)
{ return compare(r1, r2) == 1; }

bool operator!=(const real &r1, const real &r2)
{ return compare(r1, r2) != 0; }



long double compute(long double X, long double C, long double F, unsigned k)
{
    long double result = 0.0;
    for (unsigned i = 0; i < k; i++)
        result += C/(2.0 + i*F);
    result += X/(2.0 + k*F);
    return result;
}

void cookies(unsigned case_num)
{
    long double X, C, F;
    std::cin >> C >> F >> X;
    
    unsigned left = 0, right = 1000000;
    while (left + 3 < right)
    {
        unsigned left_third = left + (right - left)/3;
        unsigned right_third = right - (right - left)/3;

        assert(left_third >= left);
        assert(right_third <= right);

        real res_left = compute(X, C, F, left_third);
        real res_right = compute(X, C, F, right_third);

        if (res_left == res_right)
        {
            left = left_third;
            right = right_third;
        }
        else if (res_left > res_right)
            left = left_third;
        else if (res_left < res_right)
            right = right_third;
    }

    long double best = compute(X, C, F, left);
    for (unsigned i = 1; i <= 3; i++)
        best = std::min(best, compute(X, C, F, left + i));

    std::cout << "Case #" << case_num << ": " << best << std::endl;
}

int main()
{
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout.precision(7);

    unsigned tests;
    std::cin >> tests;
    for (unsigned i = 1; i <= tests; i++)
        cookies(i);

    return 0;
}
