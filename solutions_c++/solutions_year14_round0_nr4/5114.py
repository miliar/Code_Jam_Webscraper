#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int T;
    const int NUM = 1000;

    double a[NUM], b[NUM];
    int n;

    freopen( "codejam_D_in.txt", "r", stdin );
    freopen( "codejam_D_out.txt", "w", stdout);

    cin >> T;
    for( int t=0; t<T; t++ )
    {
        cout << "Case #" << t+1 << ": ";
        cin >> n;
        for( int i=0; i<n; i++ )
            cin >> a[i];
        for( int i=0; i<n; i++ )
            cin >> b[i];

        sort( a, a+n );
        sort( b, b+n );

        //cout << endl;
        //for( int i=0; i<n; i++ )
        //    cout << a[i] << " " << b[i] << endl;
        int p1 = 0;
        int p2 = 0;

        int q1 = 0;
        int q2 = n-1;
        int u = n-1;

        while( q1 <= q2 )
        {
            if( a[q2] > b[u] )
            {
                q2--;
                p1++;
            }
            else
            {
                q1++;
            }
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

        cout << p1 << " " << p2 << endl;
    }
}
