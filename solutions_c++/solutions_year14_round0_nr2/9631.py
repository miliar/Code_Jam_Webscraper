#define _CRT_SECURE_NO_WARNINGS

#include <iterator>
#include <fstream>
#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

typedef long double ld;

int main()
{
    ifstream in("B-small-attempt0.in");
    //freopen("output.txt", "w", stdout);

    cout.precision(20);
    cout << fixed;

    int tests;
    in >> tests;

    for (int test = 0; test != tests; ++test)
    {
        cout << "Case #" << test + 1 << ": ";

        ld c, f, x;
        in >> c >> f >> x;

        ld sum = 0.L, perSec = 2.L;
        ld one = (c / perSec) + (x / (perSec + f)), two = (x / perSec);

        while (one < two)
        {
            sum += c / perSec;
            perSec += f;

            one = (c / perSec) + (x / (perSec + f));
            two = (x / perSec);
        }

        cout << (x / perSec) + sum << "\n";
    }

    in.close();

    return 0;
}