#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

long long int current_case, t, a, b, solution;

long long int get_rev (long long int x)
{
    int rev = 0, current = x;
    while (current)
    {
        rev *= 10;
        rev += (current % 10);
        current /= 10;
    }

    return rev;
}

int main ()
{
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    scanf ("%lld", &t);
    while (t--)
    {
        int sol = 0;
        scanf ("%lld %lld", &a, &b);

        solution = 0;

        for (int i = 1; i * i <= b; i++)
            if (get_rev (i) == i && a <= i * i && i * i <= b && get_rev (i * i) == i * i)
                solution++;

        current_case++;
        printf ("Case #%lld: %lld\n", current_case, solution);
    }

    return 0;
}
