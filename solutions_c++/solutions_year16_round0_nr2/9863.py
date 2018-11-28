#include <bits/stdc++.h>

using namespace std;

bool terminado( string aComprobar , int iteradorOrdenado )
{
    //cout<<"Begin terminado\n";
    for( int voy = 0 ; voy < aComprobar.length() ; voy++ )
    {
        // cout<<"Buscando la posicion "<<voy<<endl;
        if( aComprobar[voy] == '-' )
        {
            //cout<<"Halle un menos\n";
            return false;
        }
    }
    return true;
}

void reverse_string( string &pancakes , int posicion )
{
    if( posicion != 0)
    {
        stack<char> pila;
        for( int t = 0 ; t <= posicion ; t++ )
        {
            pila.push( pancakes[t] );
        }
        int r = 0;
        while( !pila.empty() )
        {
            pancakes[r++] = pila.top();
            pila.pop();
        }
    }
}

void voltear( string &pancakes , int posicion )
{
    //cout<<"Reverse begin "<<*posicion<<endl;
    //cout<<"iterador "<<*posicionIterador<<endl;
    //cout<<"Volteando hasta "<<posicion<<endl;
    reverse_string( pancakes , posicion );
    //cout<<"Despues de voltear\n"<<pancakes<<endl;
    for( int k = 0 ; k <= posicion ; k++ )
    {
        //cout<<"comprobacion\n"<<k;
        if( pancakes[k] == '-' )
        {
            //cout<<"if\n";
            pancakes[k] = '+';
            //cout<<"ifend\n";
        }
        else if( pancakes[k] == '+' )
        {
            //cout<<"else\n";
            pancakes[k] = '-';
            //cout<<"endelse\n";
        }
        /*if( iterador == posicion )
        {
            cout<<"enditerator\n";
        }
        else
        {
            cout<<"stillIterator\n";
        }*/
    }
    //cout<<"Voltear end\n"<<pancakes<<endl;
}

int buscarPosicionSeguida( string pancakes , char aBuscar )
{
    for( int t = 0 ; t < pancakes.length() ; t++ )
    {
        if( pancakes[t] != aBuscar )
        {
            return t - 1;
        }
    }
}

int establecerIterador( string pancakes )
{
    for( int k = pancakes.length() - 1 ; k >= 0 ; k-- )
    {
        if( pancakes[k] == '-' )
        {
            return k;
        }
    }
    return 0;
}

int main()
{
    int numCasos;
    cin>>numCasos;
    cin.ignore();
    for( int k = 1 ; k <= numCasos ; k++ )
    {
        int movimientos = 0;
        string pancakes;
        getline( cin , pancakes );
        int posicionOrdenado = pancakes.length() - 1;
        //cout<<pancakes<<endl;
        while( !terminado( pancakes , posicionOrdenado ) )
        {
            int desdeDondeVoltear;
            //cout<<"Begin while\n";
            movimientos++;
            posicionOrdenado = establecerIterador( pancakes );
            //cout<<"Organizado hasta "<<posicionOrdenado<<endl;
            //cout<<"asdsada\n";
            if( pancakes[0] == '+' )
            {
                desdeDondeVoltear = buscarPosicionSeguida( pancakes , '+' );
                voltear( pancakes , desdeDondeVoltear);
            }
            else
            {
                voltear( pancakes , posicionOrdenado );
            }
            //cout<<"End while\n";
        }
        cout<<"Case #"<<k<<": "<<movimientos<<endl;
    }
    return 0;
}
