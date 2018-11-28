#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
using namespace std;

vector<double> wyniki;

int main()
{
    //fstream wyjscie;
    //wyjscie.open("wyjscie.txt", ios::out);
    int t;
    double c, f, x, wynik;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        double dodac=0, lf=0;
        cin>>c>>f>>x;
        while(true)
        {
            if((x/(2+f*lf))<=((c/(2+f*lf))+(x/(2+f*lf+f))))
            {
                wynik=(x/(2+f*lf))+dodac;
                //wyjscie<<"Case #"<<i+1<<": "<<wynik<<"\n";
                wyniki.push_back(wynik);
                break;
            }
            dodac+=c/(2+f*lf);
            lf++;
        }
    }
    for(int i=0; i<t; i++) printf("Case #%d: %0.7lf\n", i+1, wyniki[i]);
}
