#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout("magictric.txt");
    int cont = 0,casos;
    cin>>casos;
    while(casos--)
    {
        map<int,int> mapa;
        map<int,int>::iterator it;
        int fila,num,a=2;
        while(a--)
        {
            cin>>fila;
            for(int i = 0 ; i < 16 ; ++i)
            {
                cin>>num;
                if((fila == 1) && (i >= 0 && i < 4))
                    mapa[num]++;
                else if((fila == 2) && (i >= 4 && i < 8))
                    mapa[num]++;
                else if((fila == 3) && (i >= 8 && i < 12))
                    mapa[num]++;
                else if((fila == 4) && (i >= 12 && i < 16))
                    mapa[num]++;
            }
        }
        int aux=0,carta=0;
        for(it = mapa.begin() ; it!= mapa.end() ; ++it)
        {
            if(it->second == 2)
            {
                aux++;
                carta = it->first;
            }
        }
        cont++;
        if(aux == 1)
        {
            cout<<"Case #"<<cont<<":"<<" "<<carta<<endl;
        }
        else if (aux > 1)
        {
            cout<<"Case #"<<cont<<":"<<" "<<"Bad magician!"<<endl;
        }
        else
        {
            cout<<"Case #"<<cont<<":"<<" "<<"Volunteer cheated!"<<endl;
        }
    }
    cout.close();
    return 0;
}
