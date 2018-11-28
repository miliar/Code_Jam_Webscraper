#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

typedef unsigned long long uint;

bool palin(uint p)
{
    uint t = 0;
    uint cp = p;

    while(cp != 0)
    {
        t = t*10 + (cp%10);
        cp /= 10;
    }

    return (t==p);
}

int main(int argc, char *argv[])
{
    uint A,B;
    int T,cnt;


    fstream entree("fichier.txt");
    fstream sortie("sortie.txt", ios::out);

    entree >> T;
    for(int t = 0; t < T; t++)
    {
        entree >> A >> B;
        cnt = 0;
        for(uint i = ceil(sqrt(A)); i*i <= B; i++)
        {
            //cout << i << ": " << palin(i) << endl;
            if(palin(i) && palin(i*i))
             cnt++;
        }
        sortie << "Case #" << t+1 << ": " << cnt << endl;
    }
}
