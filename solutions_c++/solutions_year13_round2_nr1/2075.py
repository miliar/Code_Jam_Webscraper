#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>

#define MAX_SIZE 1100000

using namespace std;

typedef long long integer;

int main()
{
    integer T, A, N, total;
    integer * motes = new integer[ MAX_SIZE ];

    cin >> T;

    for ( integer k = 1; k <= T; k++ )
    {
        total = 0;
        cin >> A >> N;
        for ( integer i = 0; i < N; i++ )
        {
            cin >> motes[ i ];
        }
        sort( motes, motes+N );

        for ( integer i = 0; i < N; i++ )
        {
            if ( motes[ i ] < A ) A += motes[ i ];
            else
            {
                integer partial = 1;
                integer value = 2*A-1;
                if ( A == 1 )
                {
                    total += N-i;
                    break;
                }
                else
                {
                    while ( value <= motes[ i ] )
                    {
                        value = 2*value-1;
                        partial++;
                    }
                    if ( partial < N-i )
                    {
                        total += partial;
                        A = value+motes[i];
                    }
                    else
                    {
                        total += N-i;
                        break;
                    }
                }
            } 
        }

        cout << "Case #" << k <<": " << total << endl;
    }

    delete [] motes;

    return 0;
}
