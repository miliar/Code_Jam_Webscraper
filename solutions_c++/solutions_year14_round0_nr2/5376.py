#include <iostream>

#include<iomanip>

using namespace std;

#define NFARMS 100001
#define INFINITO 100000000.0
double C;
double F;
double X;

double farms[NFARMS+1][2]; // Posicion 0 llegar a C, posicion 1 llegar a X
double ncookies[NFARMS+1];// Cookies por segundo en cada estado

void resuelve(int caso)
{
    double res=INFINITO;
    int i,j,k;
    // Comienzas por 2 cookies por segundo
    ncookies[0]=2.0;
    farms[0][0]=C/ncookies[0];
    farms[0][1]=X/ncookies[0];
    
    if(res>farms[0][1])
    {
        res=farms[0][1];
    }
    
    ncookies[1]=ncookies[0]+F;
   
    for(i=1;i<NFARMS;i++)
    {
        
        farms[i][0]=(C/ncookies[i])+farms[i-1][0];
        farms[i][1]=(X/ncookies[i])+farms[i-1][0];
    
        if(res>farms[i][1])
        {
            res=farms[i][1];
        }    
        ncookies[i+1]=ncookies[i]+F;
        
        /* 
        // Caso que cueste mas llegar a la fabrica que al mejor resultado
        if(farms[i][0]>res)
        {
            break;
        }
        */
    }
    
    cout << fixed<<setprecision(7)<< "Case #"<<caso<<": "<<res<<endl;
}

int main()
{
    int T;
    int i,j,k;
    cin >> T;
    
    // Inicialmente 2 cookies por segundo
    
    for(i=0;i<T;i++)
    {
        cin >> C;
        cin >> F;
        cin >> X;
        resuelve(i+1);
    }
    return 0;
}
