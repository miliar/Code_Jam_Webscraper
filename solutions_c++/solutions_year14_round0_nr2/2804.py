#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <utility>
#include <fstream>
#include <iomanip>

#define PLUS_INFINI 100*1000

using namespace std;

int main()
{
    ifstream cin ("in.txt");
   ofstream cout ("out.txt");

    int T = 0;
    cin >> T;
cout.precision(10);
    for(int i = 1; i <= T; i++)
    {

       double C = 0, F = 0, X= 0;
        cin.precision(10);


       cin >> C;
       cin >> F;
        cin >> X;


        double freq = 2;

        double tempsX = X/freq;
        double tempsC = C/freq;

        freq += F;
        double tempsTotal = tempsC;
        double miniT = PLUS_INFINI;
        while(miniT >= tempsX)
        {
            miniT = tempsX;
            tempsX = tempsTotal +  X/freq;
            tempsTotal = tempsTotal + C/freq;
            freq += F;
        }

        cout << "Case #"<< i << ": " << miniT << endl;

    }





    return 0;
}
