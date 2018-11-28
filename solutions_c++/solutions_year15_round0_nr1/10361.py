#include <iostream>
using namespace std;
int main()
{
    int t,ile_wstalo,wynik,g,j=0;
    int tab[2000];
    char z;
    cin>>t;
    while(t--)
    {
        wynik=0;
        cin>>g;
        g++;
        cin>>z;
        ile_wstalo=z-'0';
        for(int i=1; i<g; i++)
        {
            //cout<<ile_wstalo<< " "<<wynik<<endl;
            cin>>z;
            if(ile_wstalo<i)
            {
                wynik+=i-ile_wstalo;
                ile_wstalo+=i-ile_wstalo;
            }

            ile_wstalo+=z-'0';
        }
        tab[j]=wynik;
        j++;
    }
    for(int i=0; i<j; i++)
        cout<<"Case #"<<i+1<<": "<<tab[i]<<endl;


    return 0;
}
