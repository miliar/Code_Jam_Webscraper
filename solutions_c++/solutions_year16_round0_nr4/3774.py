#include <bits/stdc++.h>


using namespace std;

long long pow (long long a, long long b)
{
    long long k = 1;
    while (b > 0)
    {
        k*=a;
        b--;
    }
    return k;
}

int main()
{
    int tests;
    cin >> tests;
    for (int h = 0; h < tests; ++h)
    {
        long long A, B, C;
        cin >> A >> B >> C;
        long long p = pow (A, B-1);
        cout << "Case #" << h+1 << ": ";
        for (long long i = 0; i < C; ++i)
        {
            cout << 1 + i*p << " ";
        }
        cout << endl;
    }
}
