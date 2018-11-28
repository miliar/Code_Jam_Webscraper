#include <iostream>
#include <string.h>
#include <map>
#include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

bool gotIt(map< char , bool> asd)
{
    int cont = 0;
    for(char k = '0' ; k <= '9' ; k++ )
    {
        if( asd.count(k) > 0 )
        {
            cont++;
        }
    }
    if( cont == 10 )
    {
            return true;
    }
    return false;
}

int main()
{
    int numCasos;
    cin>>numCasos;
    for( int t = 1 ;  t <= numCasos ; t++ )
    {
        map< char , bool> numeros;
        string resultado;
        long long numero;
        cin>>numero;
        bool cond = true;
        if( numero == 0 )
        {
            resultado = "INSOMNIA";
        }
        else
        {
            for( int t = 1 ; cond ; t++)
            {
                int nuevoNumero = numero * t;
                //cout<<nuevoNumero<<endl;
                char *intStr = new char[50];
                itoa( nuevoNumero , intStr , 10);
                string abc = string( intStr );
                for( int t = 0 ; t < abc.length() && cond ; t++ )
                {
                    numeros[ abc[t] ] = true;
                    if( gotIt( numeros ) )
                    {
                        resultado = abc;
                        cond = false;
                    }
                }
            }
        }
        cout<<"Case #"<<t<<": "<<resultado<<endl;
    }
    return 0;
}
