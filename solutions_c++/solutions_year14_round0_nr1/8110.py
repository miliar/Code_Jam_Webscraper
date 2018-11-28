#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;


int main()
{
    stringstream couta;
    int casos,j,k,aux;
    cin>>casos;
    for(int i=1;i<=casos;++i)
    {
        int resp1,resp2,cont,numero;
        cont=0;
        cin>>resp1;
        set<int> numeros;

        for(k=0;k<4;++k)
        {

            for(j=0;j<4;++j)
            {
                cin>>aux;
                if((k+1)==resp1)
                numeros.insert(aux);
            }
        }
        cin>>resp2;

        for(k=0;k<4;++k)
        {

            for(j=0;j<4;++j)
            {
                cin>>aux;
                if((k+1)==resp2)
                {
                    if(!numeros.insert(aux).second)
                    {
                        cont++;
                        numero=aux;
                    }

                }

            }
        }

        couta<<"Case #"<<i<<": ";
        if(cont==1)
        {
            couta<<numero<<endl;
        }
        else if(cont > 1)
        {
            couta<<"Bad magician!"<<endl;
        }
        else if(cont == 0)
        {
            couta<<"Volunteer cheated!"<<endl;
        }

        string myString = couta.str();
        std::ofstream myfile;
        myfile.open ("MagicTrickOUT.txt");
        myfile << myString;
        myfile.close();



    }


    return 0;
}
