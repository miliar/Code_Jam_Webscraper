#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int contador;
    int cantidad;
    int total;
    int amigos;
    char a;
    char entrada[1050];
    cin >> contador;

    int aux=contador;
    while (contador--)
    {
        cin >> cantidad >> entrada;
        total=0;
        amigos=0;
        for(int i=0;i<=cantidad;i++)
        {
            a=entrada[i];
            if (total<i)
            {
                    amigos+=i-total;
                total=i;
            }
            total+=atoi(&a);
        }//Case #1:
        cout << "Case #" << aux-contador << ":" << " " << amigos << endl;
    }

    return 0;
}
