#include <iostream>
#include <vector>

using namespace std;

int
main()
{
    int numCasos, i, j, casos;
    vector< string >juego;
    string linea, aux;
    bool hayPunto, ganado;

    cin >> numCasos;
    casos = numCasos;
    cin.ignore();

    while ( numCasos-- )
    {
        for ( i = 0; i < 4; ++i )
        {
            getline( cin, linea );
            juego.push_back( linea );
        }
        getline( cin, linea );
        hayPunto = false;
        ganado = false;
        aux = "";
        cout << "Case #";
        for ( i = 0; i < 4; ++i )
        {
            if ( juego[i] == "XXXX" || juego[i] == "XXXT" || juego[i] == "XXTX" || juego[i] == "XTXX" || juego[i] == "TXXX" )
            {
                cout << casos-numCasos << ": X won";
                ganado = true;
                break;
            }
            if ( juego[i] == "OOOO" || juego[i] == "OOOT" || juego[i] == "OOTO" || juego[i] == "OTOO" || juego[i] == "TOOO" )
            {
                cout << casos-numCasos << ": O won";
                ganado = true;
                break;
            }
            if ( !hayPunto && juego[i].find_first_of( '.' ) != string::npos )
            {
                hayPunto = true;
            }

            linea = "";
            for ( j = 0; j < 4; ++j )
            {
                linea += juego[j][i];
                if ( i == j )
                {
                    aux += juego[j][i];
                }
            }
            if ( linea == "XXXX" || linea == "XXXT" || linea == "XXTX" || linea == "XTXX" || linea == "TXXX" )
            {
                cout << casos-numCasos << ": X won";
                ganado = true;
                break;
            }
            if ( linea == "OOOO" || linea == "OOOT" || linea == "OOTO" || linea == "OTOO" || linea == "TOOO" )
            {
                cout << casos-numCasos << ": O won";
                ganado = true;
                break;
            }
        }
        if ( !ganado )
        {
            if ( aux == "XXXX" || aux == "XXXT" || aux == "XXTX" || aux == "XTXX" || aux == "TXXX" )
            {
                cout << casos-numCasos << ": X won";
                ganado = true;
            }
            if ( aux == "OOOO" || aux == "OOOT" || aux == "OOTO" || aux == "OTOO" || aux == "TOOO" )
            {
                cout << casos-numCasos << ": O won";
                ganado = true;
            }
            if ( !ganado )
            {
                aux = "";
                aux += juego[3][0];
                aux += juego[2][1];
                aux += juego[1][2];
                aux += juego[0][3];
                if ( aux == "XXXX" || aux == "XXXT" || aux == "XXTX" || aux == "XTXX" || aux == "TXXX" )
                {
                    cout << casos-numCasos << ": X won";
                    ganado = true;
                }
                if ( aux == "OOOO" || aux == "OOOT" || aux == "OOTO" || aux == "OTOO" || aux == "TOOO" )
                {
                    cout << casos-numCasos << ": O won";
                    ganado = true;
                }
                if ( !ganado )
                {
                    if ( hayPunto )
                    {
                        cout << casos-numCasos << ": Game has not completed";
                    }
                    else
                    {
                        cout << casos-numCasos << ": Draw";
                    }
                }
            }
        }
        cout << endl;
        juego.clear();
    }

    return 0;
}
