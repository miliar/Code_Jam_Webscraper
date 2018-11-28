#include <iostream>
#include <cstring>
using namespace std;

long long int N;
char cadena[10000];
char cadenaTMP[10000];
char tmp[30];

void flip(int x)
{
    int i,j;
    strcpy(cadenaTMP,cadena);
    
    for(i=0,j=x-1;i<x;i++,j--)
    {
        if(cadenaTMP[i]=='-')
        {
            cadena[j]='+';
        }
        else
        {
            cadena[j]='-';
        }
    }
}
int esSolucion()
{
    int i;
    int tam=strlen(cadena);
    
    for(i=0;i<tam;i++)
    {
        if(cadena[i]=='-')
        {
            return 0;
        }
    }
    return 1;
}
int esSolucionINV()
{
    int i;
    int tam=strlen(cadena);
    
    for(i=0;i<tam;i++)
    {
        if(cadena[i]=='+')
        {
            return 0;
        }
    }
    return 1;
}

long long int calcularMovimientos()
{
    long long int res=0;
    int i,j;
    int tam=strlen(cadena);
    
                
    if(esSolucion())
    {
        return res;
    }
                    if(esSolucionINV())
                    {
                        return res+1;
                    }
    for(i=0;i<tam;i++)
    {
        // Encontrado desorden
        if(i>0 && cadena[i]!=cadena[i-1])
        {
            //cout << "giro en "<<(i)<<" " << cadena <<endl;
            flip(i);
            //cout << "resultado giro " << cadena <<endl;
            res++;
            
            if(esSolucion())
            {
                return res;
            }
                    if(esSolucionINV())
                    {
                        return res+1;
                    }
            int encontrado=0;
            for(j=i+1;j<tam;j++)
            {
                
                if(j>0 && cadena[j]!=cadena[j-1])
                {
                    encontrado=1;
                    //cout << "giro en "<<(i+1)<<" " << cadena <<endl;
                    flip(j);
                    //cout << "resultado giro " << cadena <<endl;
                    res++;
            
                    if(esSolucion())
                    {
                        return res;
                    }
                    if(esSolucionINV())
                    {
                        return res+1;
                    }
                }
            }
            if(encontrado==0)
            {
                //cout << "giro en "<<(i+1)<<" " << cadena <<endl;
                    flip(tam-1);
                    //cout << "resultado giro " << cadena <<endl;
                    res++;
            
                    if(esSolucion())
                    {
                        return res;
                    }
                    if(esSolucionINV())
                    {
                        return res+1;
                    }
            }
        }
    }
    if(cadena[0]=='-')
    {
        
            //cout << "giro en "<<tam<<" " << cadena <<endl;
            flip(tam);
            //cout << "resultado giro " << cadena <<endl;
            res++;
    }
    return res;
}

/*
long long int calcularMovimientos()
{
    long long int res=0;
    int i,j;
    int tam=strlen(cadena);
    
    for(i=tam-1;i>=0;i--)
    {
        // Encontrado desorden
        if(cadena[i]=='-' && i>0)
        {
            if(cadena[0]=='-')
            {
                cout << "giro en 1 " << cadena <<endl;
                flip(1);
                res++;
                
                cout << "resultado giro " << cadena <<endl;
            }
            cout << "giro en "<<(i+1)<<" " << cadena <<endl;
            flip(i+1);
            cout << "resultado giro " << cadena <<endl;
            res++;
        }
        else if(cadena[i]=='-' && i==0)
        {
            cout << "giro en "<<(i+1)<<" " << cadena <<endl;
            flip(1);
            cout << "resultado giro " << cadena <<endl;
            res++;
        }
    }
    return res;
}
*/
int main()
{
    long long int res;
    int i;
    cin >> N;
    cin.getline(tmp,2);
    for(i=0;i<N;i++)
    {
        cin.getline(cadena,1000);
        res=calcularMovimientos();
        cout << "Case #"<<(i+1)<<": "<<res<<endl;
    }
    
    
    return 0;
}
