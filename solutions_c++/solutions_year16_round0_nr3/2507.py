#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

long long toBase(int bitsCount, int number, int base)
{
    long long res = 0;
    for (int i = bitsCount - 1; i >= 0; --i)
    {
        res = res * base + ((number & (1 << i)) ? 1 : 0);
    }
    return res;
}

long long getDivisor(long long number)
{
    for (long long i = 2; i * i <= number; ++i)
    {
        if (number % i == 0)
            return i;
    }
    return -1;
}

struct Ans{
    int number;
    long long divisor[11];

    bool checkDivisors(int bitsCount)
    {
        for (int base = 2; base <= 10; base++)
        {
            long long current = toBase(bitsCount, number, base);
            long long div = getDivisor(current);
            if (div == -1)
                return false;
            divisor[base] = div;
        }
        return true;
    }

    void print(int bitsCount)
    {
        for (int i = bitsCount - 1; i >= 0; --i)
        {
            printf("%d", (number & (1 << i)) ? 1 : 0);
        }

        for (int base = 2; base <= 10; base++)
        {
            printf(" %lld", divisor[base]);
        }
        printf("\n");
    }
};

int combine(int m1, int m2)
{
    return m1 | (m2 << 1);
}

void solve(int n, int j)
{
    vector<Ans> result(j);
    int mask = (1 << (n - 1)) + 1;
    int count = 0;
    for (int m = 0; m < (1 << (n - 2)) && count < j; m++)
    {
        result[count].number = combine(mask, m);
        if (result[count].checkDivisors(n))
            count++;
    }
    for (int i = 0; i < j; ++i)
    {
        result[i].print(n);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d", &q);
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d:\n", t);
        int n, j;
        scanf("%d%d", &n, &j);
        solve(n, j);
    }
    return 0;
}