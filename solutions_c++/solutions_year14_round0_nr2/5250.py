#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T, r, x, ans;
    const int NUM = 17;
    bool numbers[NUM];

    freopen( "codejam_A_in.txt", "r", stdin );
    freopen( "codejam_A_out.txt", "w", stdout);

    cin >> T;
    for( int t=0; t<T; t++ )
    {
        fill_n( numbers, NUM, 0 );
        ans = 0;
        cout << "Case #" << t+1 << ": ";

        cin >> r;
        for( int i=0; i<4*(r-1); i++ )
            cin >> x;
        for( int i=0; i<4; i++ )
        {
            cin >> x;
            numbers[x] = true;
        }
        for( int i=4*r; i<16; i++ )
            cin >> x;

        cin >> r;
        for( int i=0; i<4*(r-1); i++ )
            cin >> x;
        for( int i=0; i<4; i++ )
        {
            cin >> x;
            if( numbers[x] )
            {
                if( !ans )
                    ans = x;
                else
                {
                    ans = -1;
                }
            }
        }
        for( int i=4*r; i<16; i++ )
            cin >> x;

        if( ans > 0 )
            cout << ans << endl;
        else if ( !ans )
            cout << "Volunteer cheated!\n";
        else
            cout << "Bad magician!\n";
    }
}
