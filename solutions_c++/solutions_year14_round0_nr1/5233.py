#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T, r, a, rez;
    bool nums[17];

    freopen( "qualA.in", "r", stdin );
    freopen( "qualA.out", "w", stdout);

    cin >> T;
    for( int t=0; t<T; t++ )
    {
        cout << "Case #" << t+1 << ": ";

        fill_n( nums, 17, 0 );
        rez = 0;

        cin >> r;

        for( int i=0; i<4*(r-1); i++ )
            cin >> a;

        for( int i=0; i<4; i++ )
        {
            cin >> a;
            nums[a] = true;
        }
        for( int i=4*r; i<16; i++ )
            cin >> a;

        cin >> r;
        for( int i=0; i<4*(r-1); i++ )
            cin >> a;
        for( int i=0; i<4; i++ )
        {
            cin >> a;
            if( nums[a] )
            {
                if( !rez )
                    rez = a;
                else
                {
                    rez = -1;
                }
            }
        }
        for( int i=4*r; i<16; i++ )
            cin >> a;

        if( rez > 0 )
            cout << rez << endl;
        else if ( !rez )
            cout << "Volunteer cheated!\n";
        else
            cout << "Bad magician!\n";
    }
}
