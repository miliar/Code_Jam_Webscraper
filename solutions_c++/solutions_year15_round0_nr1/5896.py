#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int
main()
{
    int numC, nivelMaximo, levantados, invitar, invitados, caso = 1, nivel, n;
    char c;

    cin >> numC;

    while( numC-- )
    {
        cin >> nivelMaximo;
        cin.ignore();
        cin >> c;
        levantados = c - 48;
        invitados = 0;
        for ( nivel = 1; nivel <= nivelMaximo; ++nivel  )
        {
            invitar = 0;
            cin.get( c );
            n = c - 48;
            if( n == 0 )
            {
                continue;
            }
            if( nivel > levantados )
            {
                invitar = nivel - levantados;
                invitados += invitar;
            }
            levantados += n + invitar;
        }
        cout << "Case #" << caso++ << ": " << invitados << endl;
    }

    return 0;
}
