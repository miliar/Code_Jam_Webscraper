#include <iostream>
#include <string>
using namespace std;
void Ultimo_Menos(string &a,int b);
void Primero_Mas(string &a,int b,int c,int d);

int main()
{
    int veces,mas,menos,casos;
    string caras;
    bool seguir;
    cin>>veces;

    for (int i=0; i<veces; i++)
    {
        cin>>caras;
        mas=0;
        menos=0;
        casos=0;
        seguir=true;

        for(int j=0; j<caras.size(); j++)
        {
            if(caras[j]=='+')
                mas++;
            if(caras[j]=='-')
                menos++;
        }

        if(mas==caras.size())
        {
            seguir=false;
            casos=0;
        }

        else
        {

            if(menos==caras.size())
            {
                seguir=false;
                for(int j=0; j<caras.size(); j++)
                {
                    caras[j]='+';
                }
                casos=1;
            }
        }


            if(caras[(caras.size()-1)]=='-')              //     VOLTEA TODO
            {
                for(int j=0; j<caras.size(); j++)
                {
                    if(caras[j]=='+')
                    {
                        caras[j]=='-';
                    }
                    else
                    {
                        caras[j]=='+';
                    }
                }
                casos++;
            }
                while(seguir==true)
                {
                    seguir=false;

                    if(caras[0]=='+')                           //VOLTEA TODOS LOS POSITIVOS HASTA LLEGAR A UN NEGATIVO, EN NEGATIVOS
                    {
                        for(int j=1; j<caras.size(); j++)
                        {
                            if(caras[j]=='-')
                            {
                                for(int h=0; h<j; h++)
                                {
                                    caras[h]='-';
                                }
                                casos++;
                                seguir=true;
                                break;
                            }
                        }
                    }
                    if(caras[0]=='-')                           //VOLTEA TODOS LOS NEGATIVOS, HASTA LLEGAR A UN POSITIVO, EN POSITIVOS
                    {
                        for(int j=1; j<caras.size(); j++)
                        {
                            if(caras[j]=='+')
                            {
                                for(int h=0; h<j; h++)
                                {
                                    caras[h]='+';
                                }
                                seguir=true;
                                casos++;
                                break;
                            }
                        }

                    }
                }
                cout<<"Case #"<<i+1<<": "<<casos<<endl;

    }
}


