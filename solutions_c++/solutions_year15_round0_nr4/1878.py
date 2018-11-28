#include <iostream>

using namespace std;

int main()
{
    int z;
    cin >> z;
    int o = 1;
    while( z -- )
    {
        int x, r, c;
        cin >> x >> r >> c;
        if( x == 1 )
        {
            cout << "Case #" << o << ": GABRIEL\n";
        }
        if( x == 2 )
        {
            if( r*c % 2 == 0 )   cout << "Case #" << o << ": GABRIEL\n";
            else cout << "Case #" << o << ": RICHARD\n";
        }
        if( x == 3 )
        {
            if( r*c % 3 == 0 && r*c > 3 ) cout << "Case #" << o << ": GABRIEL\n";
            else cout << "Case #" << o << ": RICHARD\n";
        }
        if( x == 4 )
        {
            if( r*c == 16 || r*c == 12 ) cout << "Case #" << o << ": GABRIEL\n";
            else cout << "Case #" << o << ": RICHARD\n";
        }
        o ++;
    }
    return 0;
}
