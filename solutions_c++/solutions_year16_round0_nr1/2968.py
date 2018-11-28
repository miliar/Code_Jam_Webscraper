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

bool digits[10];
int digitsCount;

void check(int m)
{
    while (m)
    {
        digitsCount += !digits[m % 10];
        digits[m % 10] = true;
        m /= 10;
    }
}

int solve(int n)
{
    memset(digits, false, sizeof(digits));
    digitsCount = 0;
    int m = n;
    while (digitsCount < 10)
    {
        check(m);
        m += n;
    }
    return m - n;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d", &q);
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d: ", t);
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        printf("%d\n", solve(n));
    }
    return 0;
}