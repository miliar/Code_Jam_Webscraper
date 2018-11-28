#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <utility>
#include <fstream>


using namespace std;

int tab[5];

int main()
{
    ifstream cin ("in.txt");
    ofstream cout ("out.txt");


    int T = 0;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        int R1, R2;
       cin >> R1;
        for(int iCarte = 1; iCarte <= 4;iCarte++)
            for(int jCarte = 1; jCarte <= 4; jCarte++)
            {
                int carte;
                cin >> carte;
                if(iCarte == R1)
                    tab[jCarte] = carte;
            }

       cin >> R2;
        int compteur = 0;
        int carteChoisie = 0;
        for(int iCarte= 1; iCarte <= 4; iCarte++)
            for(int jCarte = 1; jCarte <=4; jCarte++)
            {
                int carte;
                cin >> carte;
                if(iCarte == R2)
                {
                    for(int iCarte1 = 1; iCarte1 <=4; iCarte1++)
                    {
                        if(carte == tab[iCarte1])
                        {
                            compteur++;
                            carteChoisie = carte;
                        }
                    }
                }

            }

        if(compteur == 0)
           cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
       else if(compteur == 1)
            cout <<"Case #" << i+1 <<": " << carteChoisie << endl;
       else
            cout <<"Case #" << i+1 << ": Bad magician!" << endl;
    }





    return 0;
}
