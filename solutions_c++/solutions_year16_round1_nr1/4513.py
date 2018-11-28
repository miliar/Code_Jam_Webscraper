#include <bits/stdc++.h>

using namespace std;

void ganadora( string aEvaluar , vector<string> &soluciones , int indice , string palabra )
{
    if( palabra.length() == aEvaluar.length() )
    {
        soluciones.push_back(palabra);
        return;
    }
    ganadora( aEvaluar , soluciones , indice + 1 , palabra + aEvaluar[indice] );
    ganadora( aEvaluar , soluciones , indice + 1 , aEvaluar[indice] + palabra );
}

int main()
{
    int numCasos;
    cin>>numCasos;
    cin.ignore();
    for( int k = 1 ; k <= numCasos ; k++ )
    {
        string s ;
        vector<string> soluciones;
        getline( cin , s );
        string nuevo;
        nuevo.push_back(s[0]);
        ganadora( s  , soluciones , 1 , nuevo );
        sort( soluciones.rbegin() , soluciones.rend() );
        cout<<"Case #"<<k<<": "<<soluciones[0]<<endl;
    }
}
