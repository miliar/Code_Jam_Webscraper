#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    int N,N2,N3,N4;
    cin>>T;
    int j=0;
    bool seguir=true,seguir1;
    int arreglo[10];
    for(int i=0; i<T; i++)
    {
        j=0;
        cin>>N;
        seguir=true;
        seguir1=true;
        for(int h=0;h<10;h++)
        {
            arreglo[h]=-1;
        }
        while(seguir==true && seguir1 == true)
        {
            j++;
            N3=j*N;
            if(N3==0)
            {
                cout<<"Case #"<<i+1<<": INSOMNIA";
                seguir=false;
            }
            else
            {
                while(N3!=0)
                {
                    N2=N3%10;
                    N3=N3/10;
                    arreglo[N2]=N2;
                    if(arreglo[0]==0 && arreglo[1]==1 && arreglo[2]==2 && arreglo[3]==3 && arreglo[4]==4 && arreglo[5]==5 && arreglo[6]==6 && arreglo[7]==7 && arreglo[8]==8 && arreglo[9]==9)
                    {
                        seguir1=false;
                    }
                }
            }

        }

        if(seguir1==false)
        {
            cout<<"Case #"<<i+1<<": "<<j*N;
        }
        cout<<endl;
    }
}



