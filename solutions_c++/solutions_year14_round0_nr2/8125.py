#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout("cookieclicker.txt");
    int casos,cont = 0;
    cin>>casos;
    while(casos--)
    {
        double valorgranja,aumento,meta;
        double segundo = 2.0;
        double tiempo = 0.0,aux = 0.0,tiempo4 = 0.0;
        double menort = 100000000000000;
        map<double,int> mapa;
        map<double,int>::iterator it;
        bool bandera = false;

        cin>>valorgranja>>aumento>>meta;

        while(bandera == false)
        {
            double tiempo1 = 0,tiempo3 = 0;
            tiempo1 = (meta / segundo) + tiempo;
            tiempo+= valorgranja/segundo;
            if(tiempo1 >= tiempo)
            {
                segundo+= aumento;
            }
            if(tiempo1 < menort)
            {
                menort = tiempo1;
            }
            else
            {
                bandera = true;
                aux = menort;
                break;
            }
          /*  mapa[menort]++;
            for(it = mapa.begin(); it!= mapa.end(); ++it)
            {
                if(it->second == 2)
                {
                    bandera = true;
                    aux = it->first;
                    break;
                }
            }*/
        }
        cont++;
        cout<<fixed;
        cout<<setprecision(7)<<"Case #"<<cont<<":"<<" "<<aux<<endl;
    }
    cout.close();
    return 0;
}
