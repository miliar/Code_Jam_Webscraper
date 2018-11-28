#include <iostream>
#include <cstdio>
using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define dforn(i,n) for(int i=(n-1);i>=0;i--)

int ganadoras[][4] = {  {0,1,2,3},
                        {4,5,6,7},
                        {8,9,10,11},
                        {12,13,14,15},
                        {0,4,8,12},
                        {1,5,9,13},
                        {2,6,10,14},
                        {3,7,11,15},
                        {0,5,10,15},
                        {3,6,9,12}
                     };

char pos[16];

bool gano ( char X )
{
    bool capazGana = true;
    forn(i,10)
    {
        capazGana = true;
        forn(j,4)
        {
            if ( pos[ganadoras[i][j]] != 'T' && pos[ganadoras[i][j]] != X )
            {
                capazGana = false;
            }
        }
        if( capazGana )
        {
            return true;
        }
    }
    return false;
}

int main ()
{
    freopen("tictactoe.in","r",stdin);
    freopen("tictactoe.out","w",stdout);
    int T, cantPuntos;
    char aux;
    cin >> T;
    forsn(caso,1,T+1)
    {
        cantPuntos = 0;
        forn(i,4)
        {
            forn(j,4)
            {
                cin >> aux;
                pos[i+4*j] = aux;
                if( aux == '.' )
                {
                    cantPuntos++;
                }
            }
        }

        if( gano('X') )
        {
            cout << "Case #" << caso << ": X won" <<endl;
        }
        else if ( gano('O') )
        {
            cout << "Case #" << caso << ": O won" <<endl;
        }
        else if ( cantPuntos == 0 )
        {
            cout << "Case #" << caso << ": Draw" <<endl;
        }
        else
        {
            cout << "Case #" << caso << ": Game has not completed"<<endl;
        }
    }
    return 0;
}
