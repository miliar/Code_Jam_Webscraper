#include <iostream>
#include <string>

using namespace std;

pair < bool, int > P;

int tab[4][4][2]; //znak,  wynik

int main()
{
    tab[0][0][0] = 0;
    tab[0][0][1] = 0;
    tab[0][1][0] = 0;
    tab[0][1][1] = 1;
    tab[0][2][0] = 0;
    tab[0][2][1] = 2;
    tab[0][3][0] = 0;
    tab[0][3][1] = 3;
    
    tab[1][0][0] = 0;
    tab[1][0][1] = 1;
    tab[1][1][0] = 1;
    tab[1][1][1] = 0;
    tab[1][2][0] = 0;
    tab[1][2][1] = 3;
    tab[1][3][0] = 1;
    tab[1][3][1] = 2;
    
    tab[2][0][0] = 0;
    tab[2][0][1] = 2;
    tab[2][1][0] = 1;
    tab[2][1][1] = 3;
    tab[2][2][0] = 1;
    tab[2][2][1] = 0;
    tab[2][3][0] = 0;
    tab[2][3][1] = 1;
    
    
    tab[3][0][0] = 0;
    tab[3][0][1] = 3;
    tab[3][1][0] = 0;
    tab[3][1][1] = 2;
    tab[3][2][0] = 1;
    tab[3][2][1] = 1;
    tab[3][3][0] = 1;
    tab[3][3][1] = 0;
    
    int t;
    cin>>t;
    for(int tset = 1; tset <= t; tset++)
    {
        long long l, x, akt, stan = 0;
        string s;
        cin>>l>>x>>s;
        pair < bool, int > Para;
        Para.first = 0;
        Para.second = 0;
        for(int j=0; j<x; j++)
        {
            for(int i=0; i<l; i++)
            {
                if (s[i] == 'i')
                    akt = 1;
                if (s[i] == 'j')
                    akt = 2;
                if (s[i] == 'k')
                    akt = 3;
                Para.first ^= tab[Para.second][akt][0];
                Para.second = tab[Para.second][akt][1];
                if (stan == 0 && Para.first == 0 && Para.second == 1)
                    stan = 1;
                if (stan == 1 && Para.first == 0 && Para.second == 3)
                    stan = 2;
       //         cout << Para.first << " " << Para.second  <<" " << stan<< endl;
            }
        }
        if (Para.first == 0 || Para.second != 0 || stan < 2)
            cout <<"Case #" << tset << ": NO\n";
        else
            cout <<"Case #" << tset <<": YES\n";
        
        
    }
  //  system("PAUSE");
    return 0;
}
    
