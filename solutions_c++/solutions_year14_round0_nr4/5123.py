#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T;
    const int NUM = 100;

    double a[NUM], b[NUM];
    int n, p1, p2, q1, q2 , u ;


    freopen( "qualD.in", "r", stdin );
    freopen( "qualD.out", "w", stdout);

    cin >> T;
    for( int t=0; t<T; t++ )
    {
        cin >> n;
        for( int i=0; i<n; i++ )
            cin >> a[i];
        for( int i=0; i<n; i++ )
            cin >> b[i];

        sort( a, a+n );
        sort( b, b+n );

        p1 = 0;
        p2 = 0;

        q1 = 0;
        q2 = n-1;
        u = n-1;

        while( q1 <= q2 )
        {
            if( a[q2] > b[u] )
            {
                q2--;
                p1++;
            }
            else
                q1++;
            u--;
        }


        string s = "";
        for( int i=0; i<n; i++ )
            s += (char)i;

        for( int i=0; i<n; i++ )
        {
            int j=0;
            for( ; j<s.size() && a[i] > b[ (int)s[j] ]; j++ );
            if( j == s.size() ) p2++;
            else s = s.erase(j,1);
        }

        cout << "Case #" << t+1 << ": " << p1 << " " << p2 << endl;
    }
}
