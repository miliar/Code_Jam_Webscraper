#include <bits/stdc++.h>

using namespace std;

void get_limits( int, int&, int& );

long long interp_base( unsigned int, int );

long long div(long long);

int main()
{
    int n = 16, j = 50;

    int low, high;
    get_limits(n, low, high);

    int count = 0;
    cout << "Case #1:" << endl;

    for ( int i = low ; i <= high && count < j ; i += 2 )
    {
        vector<long long> divs(9);

        long long num;
        for ( int base = 2 ; base <= 10 ; ++ base )
        {
            num = interp_base( i, base );

            long long d = div(num);

            if ( d == 1 ) break;

            divs[base - 2] = d;
        }

        if ( divs.back() )
        {
            ++ count;

            cout << num;

            for ( long long &l : divs )
            {
                cout << ' ' << l;
            }
            cout << endl;
        }
    }
    return 0;
}

long long interp_base( unsigned int n, int base )
{
    long long num = 0;

    long long mul = 1;

    while ( n )
    {
        if ( n & 1 )
            num += mul;
        mul *= base;
        n >>= 1;
    }
    return num;
}

void get_limits( int n, int &low, int &high )
{
    low = ( 1 << ( n - 1 ) );
    high = ( low << 1 ) - 1;
    ++ low;
}

long long div(long long num)
{
    const long long s = sqrt(num);

    for ( long long i = 2 ; i <= s ; ++ i )
    {
        if ( num % i == 0 )
            return i;
    }
    return 1;
}
