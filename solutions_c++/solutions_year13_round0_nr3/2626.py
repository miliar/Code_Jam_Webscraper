#include <iostream>
#include <cmath>
using namespace std;

bool fair(int n)
{
    int reverse = 0, N = n;
    while (n > 0)
    {
        reverse = reverse * 10 + n % 10;
        n = n / 10;
    }
    return N == reverse;
}

bool fair_and_square(int n)
{
    if (!fair(n)) return false;
    int s = (int) sqrt((double) n);
    return (s * s == n) && (fair(s));
}

int main()
{
    int n, N, a, b, i, c;
    cin >> N;
    for (n = 1; n <= N; n++)
    {
        cin >> a >> b;
        c = 0;
        for (i = a; i <= b; i++)
            if (fair_and_square(i)) c++;
        cout << "Case #" << n << ": " << c << endl;
    }
}
