#include <iostream>
#include <cstring>

using namespace std;

long long int sMax;
char cadena[10000];
long long int S[10000];

void leeCaso()
{
    cin >> sMax;
    cin.getline(cadena,2000);
    /*
    cout << sMax << endl;
    cout << cadena << endl;
    */
    // Pasamos a vector
    int tam=strlen(cadena);
    
    int i,j;
    // Condicion > 0 para ignorar el caracter espacio del principio
    for(i=1,j=0;i<tam;i++,j++)
    {
        S[j]=cadena[i]-'0';
        
        //cout << "CASO "<<j<<" " << S[j]<<endl;
    }
    
    
}

long long int resultado()
{
    long long int r=0;
    long long int l=0;
    
    int i,j,k;
    
    for(i=0;i<=sMax;i++)
    {
        if(S[i]>0)
        {
            if(l>=i)
            {
                l=l+S[i];
            }
            else
            {
                //cout << "SUmo "<<(i-l)<<" en i " <<i<<endl;
                r=r+(i-l);
                l=l+(i-l)+S[i];
            }
        }
    }
    
    
    return r;
}

int main()
{
    int T;
    
    int i;
    long long int r;
    
    cin >> T;
    
    for(i=0;i<T;i++)
    {
        leeCaso();
        r=resultado();
        cout << "Case #"<<(i+1)<<": "<<r<<endl;
    }
    
    
    return 0;
}
