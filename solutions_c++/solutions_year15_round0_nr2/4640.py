#include <iostream>

using namespace std;

long long int dMax;
long long int pdMax;
long long int D[100000];
long long int resultadoFinal;

long long int vMax,posvMax;

void leeCaso()
{
    resultadoFinal=0;
    cin >> dMax;
    int i;
    for(i=0;i<dMax;i++)
    {
        cin >> D[i];
        if(D[i]>resultadoFinal)
        {
            resultadoFinal=D[i];
        }
    }
}

void comer()
{
    int i;
    for(i=0;i<dMax;i++)
    {
        D[i]--;
    }

}
void descomer()
{
    int i;
    for(i=0;i<dMax;i++)
    {
        D[i]++;
    }

}
/*
void copiaPD()
{
    int i;
    for(i=0;i<dMax;i++)
    {
        PD[i]=D[i];
    }
    pdMax=dMax;

}

void restauraPD()
{
    int i;
    for(i=0;i<pdMax;i++)
    {
        D[i]=PD[i];
    }
    dMax=pdMax;

}
*/

void seleccionarVmax()
{
    int i;
    vMax=0;
    for(i=0;i<dMax;i++)
    {
        if(D[i]>vMax)
        {
            vMax=D[i];
            posvMax=i;
        }
    }
    if(vMax<0)
    {
        vMax=0;
    }

}


int obtenerMenor(int pivote)
{
    int i;
    int menor=9;
    int posmenor=-1;
    for(i=0;i>dMax;i++)
    {
        if(D[i]<menor && D[i]>0 && i!=pivote)
        {
            menor=D[i];
            posmenor=i;
        }
    }
    return posmenor;

}

long long int obtenrPDividida()
{
    seleccionarVmax();
    if(vMax<2)
    {
        return -1;
    }
    return posvMax;
}

long long int dividir(int casilla)
{
    seleccionarVmax();
  
    
      if(vMax%2==0)
        {
            D[posvMax]=(int)(vMax/2);
            
            if(casilla>=dMax)
            {
               D[casilla]=(int)(vMax/2);
                dMax++;
            }
            else
            {
                
                D[casilla]=D[casilla]+(int)(vMax/2);
            }
        }
        else
        {
            D[posvMax]=((int)(vMax/2))+1;
            if(casilla>=dMax)
            {
                D[casilla]=(int)(vMax/2);
                dMax++;
            }
            else
            {
                D[casilla]=D[casilla]+(int)(vMax/2);
            }
        }
    return (int)(vMax/2);
    
}
void desdividir(int p,int casilla,int r)
{
    if(r<0)
    {
        r=0;
    }
    D[p]=D[p]+r;
    D[casilla]=D[casilla]-r;
    
    if(casilla>=dMax-1)
    {
        dMax--;
    }
}


long long int esSolucion()
{
    for(int i=0;i<dMax;i++)
    {
        if(D[i]>0)
        {
        return 0;
       }
    }   
    return 1;
}


void imprimeEstado(int p, char *m)
{
    /*
    cout << "Estado => " << m <<  endl;
    cout << "ResultadoFinal => " << resultadoFinal <<  endl;
    cout << "Pasos : " << p << " dMax "<<dMax<< endl;
    for(int i=0;i<dMax;i++)
    {
        cout << D[i] << " " ;    
    }    
    cout << endl << "------------------" << endl;
   */
}



void resultado(int pasos)
{
    
    if(pasos>=resultadoFinal)
    {
        return;
    }
    
    long long int r1,r2;
 
    imprimeEstado(pasos,"COMO");
    comer();
    
    imprimeEstado(pasos+1,"HE COMIDO");
    if(esSolucion())
    {
        if(pasos+1<resultadoFinal)
        {
            resultadoFinal=pasos+1;
        }
        //cout << "===> SOLUCION en "<<(pasos+1) << " con resultadoFinal " << resultadoFinal<<endl; 
        descomer();
    
        imprimeEstado(pasos,"HE DESCOMIDO Y DIVIDO");
        return;
    }
    
    resultado(pasos+1);
    
    
    descomer();
    
    imprimeEstado(pasos,"HE DESCOMIDO Y DIVIDO");
    
    
    int pDividida=obtenrPDividida();
    
    if(pDividida!=-1)
    {            
        
            /// CASO NUEVO
            //cout << "Divido desde "<<pDividida<< " hacia " << dMax << endl;
            int cuanto=dividir(dMax);
            imprimeEstado(pasos+1,"HE DIVIDIDO");
    
            resultado(pasos+1);
            
            //cout << "DESDivido desde "<<pDividida<< " hacia " << dMax << endl;
            desdividir(pDividida,dMax,cuanto);
    
            imprimeEstado(pasos,"HE DESDIVIDIDO");
            /// CASO MENOR
            int i=obtenerMenor(pDividida);
            if(i!=-1)
            {
                //cout << "Divido desde "<<pDividida<< " hacia " << i << endl;
                int cuanto=dividir(i);
                imprimeEstado(pasos+1,"HE DIVIDIDO");
    
                resultado(pasos+1);
                
                //cout << "DESDivido desde "<<pDividida<< " hacia " << i << endl;
                desdividir(pDividida,i,cuanto);
    
                imprimeEstado(pasos,"HE DESDIVIDIDO");
            }
    
    }    
    
     
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
        resultado(0);
        cout << "Case #"<<(i+1)<<": "<<resultadoFinal<<endl;
    }
    
    
    return 0;
}
