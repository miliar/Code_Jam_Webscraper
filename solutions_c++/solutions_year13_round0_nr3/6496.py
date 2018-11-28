#include <iostream>
#include <math.h>

using namespace std;
bool VerificacaoPalindromo ( int n );

int main()
{
    int n,x,y,z=0,raiz=0,cont=0;
    cin >> n;
    while(z<n)
    {
            cin >> x;
            cin.ignore();
            cin >> y;
        cont=0;
            for(int i=x;i<=y;i++)
            {
                if(VerificacaoPalindromo(i))
                {
                    raiz = sqrt(i);
                    if(raiz*raiz==i)
                    {
                        if(VerificacaoPalindromo(raiz))
                            cont++;
                    }
                }
            }
            cout << "Case #" << z+1 << ": " << cont << "\n";
            z++;
    }

    return(0);
}

bool VerificacaoPalindromo ( int n ){

int aux;
int GuardaNumero;

aux = n;
GuardaNumero = 0;

while (aux != 0) {

GuardaNumero = GuardaNumero *10 +aux % 10;
aux = aux /10;
}

if ( GuardaNumero == n)
return true;
else return false;
}
