#include <bits/stdc++.h>

using namespace std;


int main()
{

    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);

    int T , z = 0 ;
    cin >> T;
    while( T--)
    {
        long long n , x  ;
        cin >> n ;
        long long arr[10] , m = n , c = 1 ;

        memset( arr , 0 , sizeof arr ) ;

        while( 8 )
        {
            int ch = 1 ;
            for(int i=0 ; i<10 ; i++)
                if( arr[i] == 0 )
                    ch = 0;

            if( ch || n == 0 )
            {
                cout << "Case #" << ++z << ": " ;
                if ( n == 0 ) cout << "INSOMNIA\n";
                else cout << n << "\n";
                break ;
            }

            n = m*c++ ;
            x = n ;

            while( x != 0 )
            {
                arr[ x%10 ] = 1 ;
                x /= 10 ;
            }
        }
    }
}

