#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

int
main()
{
    vector< vector< vector<bool> > >soluciones;
    int i, j, caso = 1, numC, X;

    for( i = 0; i < 4; ++i )
    {
        soluciones.push_back( vector< vector<bool> >( 4, vector<bool>( 4, false ) ) );
    }
    soluciones[0][0][0] = true;
    soluciones[0][1][0] = true;
    soluciones[0][1][1] = true;
    soluciones[0][2][0] = true;
    soluciones[0][3][0] = true;
    soluciones[0][3][1] = true;

    soluciones[1][0][0] = true;
    soluciones[1][0][1] = true;
    soluciones[1][1][0] = true;
    soluciones[1][1][1] = true;
    soluciones[1][2][0] = true;
    soluciones[1][2][1] = true;
    soluciones[1][2][2] = true;
    soluciones[1][3][0] = true;
    soluciones[1][3][1] = true;

    soluciones[2][0][0] = true;
    soluciones[2][1][0] = true;
    soluciones[2][1][1] = true;
    soluciones[2][1][2] = true;
    soluciones[2][2][0] = true;
    soluciones[2][2][2] = true;
    soluciones[2][3][0] = true;
    soluciones[2][3][1] = true;
    soluciones[2][3][2] = true;
    soluciones[2][3][3] = true;

    soluciones[3][0][0] = true;
    soluciones[3][0][1] = true;
    soluciones[3][1][0] = true;
    soluciones[3][1][1] = true;
    soluciones[3][2][0] = true;
    soluciones[3][2][1] = true;
    soluciones[3][2][2] = true;
    soluciones[3][2][3] = true;
    soluciones[3][3][0] = true;
    soluciones[3][3][1] = true;
    soluciones[3][3][3] = true;

    cin >> numC;

    while( numC-- )
    {
        cin >> X >> i >> j;

        cout << "Case #" << caso++ << ": ";
        if( soluciones[i-1][j-1][X-1] )
        {
            cout << "GABRIEL";
        }
        else
        {
            cout << "RICHARD";
        }
        cout << endl;
    }

    return 0;
}
