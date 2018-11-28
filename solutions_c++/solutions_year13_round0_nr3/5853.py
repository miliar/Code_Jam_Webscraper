#include <iostream>
#include <cmath>

using namespace std;

bool poly(int a)
{
    short int s[1000];
    int i = 0, k = 0;
    while (a > 0)
    {
        s[i] = a % 10;
        a /= 10;
        i++;
    }
    for (int j = 1; j <= i / 2; ++j)
    {
        if (s[i - j] == s[j - 1])
        {
            k += 2;
        }
    }
    if (i % 2 == 1)
        k++;
    return (k == i);
}

int main()
{
    int t, a, b, kol;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        cin >> a >> b;
        kol = 0;
        for (int j = a; j <= b; ++j)
        {
            if (trunc(sqrt(j)) == sqrt(j))
                if ((poly(j) || (j < 10)) && (poly(sqrt(j)) || (sqrt(j) < 10)))
                {
                    kol++;
                }
        }
        cout << "Case #" << i + 1 << ": " << kol << endl;
    }
}
