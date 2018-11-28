#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

inline bool isPolindrome(long long x)
{
    long long y = x, z = 0;
    while(y)
    {
        z = z * 10 + y % 10;
        y /= 10;
    }
    return x == z;
}

vector<long long> fineAndSquare;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;

    scanf("%d", &t);

    for (int i = 0; i <= 10000000; ++i)
        if (isPolindrome(i) && isPolindrome((long long)i*i))
            fineAndSquare.push_back(i);

    for (int i = 1; i <= t; ++i)
    {
        long long a, b, count = 0;
        scanf("%lld%lld", &a, &b);
        double sqrt_a = sqrt(double(a)), sqrt_b = sqrt(double(b));
        long long l = sqrt_a, r = sqrt_b;
        while (l*l < a) ++l;
        while (r*r > b) --r;
        for (int j = 0; j < fineAndSquare.size(); ++j)
            count += (l <= fineAndSquare[j] && fineAndSquare[j] <= r);
        printf("Case #%i: %i\n", i, count);
    }
    
    return 0;
}