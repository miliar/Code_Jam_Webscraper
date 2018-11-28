#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout("magiccard.txt");
    int casos,num,cartas,conta = 1;
    cin>>casos;
    while(casos--)
    {
        int cont = 2;
        map<int,int> mapa;
        map<int,int>::iterator it;
        vector<int> arreglo;
        while(cont--)
        {
            cin>>num;
            for(int i = 0 ; i < 16 ; i++)
            {
                cin>>cartas;
                if(num == 1 && ((i >= 0) && (i < 4)))
                {
                    mapa[cartas]++;
                }
                else if(num == 2 && ((i >= 4) && (i < 8)))
                {
                    mapa[cartas]++;
                }
                else if(num == 3 && ((i >= 8) && (i < 12)))
                {
                    mapa[cartas]++;
                }
                else if(num == 4 && ((i >= 12) && (i < 16)))
                {
                    mapa[cartas]++;
                }

            }
        }
        int aux = 0,carta = 0;
        for(it = mapa.begin() ; it!= mapa.end() ; ++it)
        {
            if(it->second == 2)
            {
                aux++;
                carta = it->first;
            }
        }
        if(aux == 1)
        {
            cout<<"Case #"<<conta<<": "<<carta<<endl;
        }
        else if(aux > 1)
        {
            cout<<"Case #"<<conta<<": "<<"Bad magician!"<<endl;

        }
        else if (aux == 0)
        {
            cout<<"Case #"<<conta<<": "<<"Volunteer cheated!"<<endl;

        }
        conta++;

    }
    cout.close();
    return 0;
}
