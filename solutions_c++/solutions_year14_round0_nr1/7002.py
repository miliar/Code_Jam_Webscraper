#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t, x, y, a;
    bool m1[17], m2[17];
    fstream plik, wyjscie;
    plik.open("A_small-attempt0.txt", ios::in);
    wyjscie.open("wyjscie.txt", ios::out);
    cin>>t;
    for(int i=0; i<t; i++)
    {
        int wynik=0, liczba=0;
        for(int j=0; j<17; j++)
        {
            m1[j]=false;
            m2[j]=false;
        }
        cin>>x;
        for(int j=1; j<=4; j++)
        {
            for(int k=1; k<=4; k++)
            {
                cin>>a;
                if(j==x) m1[a]=true;
            }
        }
        cin>>y;
        for(int j=1; j<=4; j++)
        {
            for(int k=1; k<=4; k++)
            {
                cin>>a;
                if(j==y) m2[a]=true;
            }
        }
        for(int j=1; j<17; j++)
            if(m1[j] && m2[j])
            {
                wynik=j;
                liczba++;
            }
        if(liczba==0) wyjscie<<"Case #"<<i+1<<": Volunteer cheated!\n";
        if(liczba==1) wyjscie<<"Case #"<<i+1<<": "<<wynik<<"\n";
        if(liczba>1) wyjscie<<"Case #"<<i+1<<": Bad magician!\n";

    }
}
