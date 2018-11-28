#include <iostream>
using namespace std;

int a[5][5],ah[5][5],b,c,d,e,f,g, berapa, apa;

int main()
{
    cin >> b;
    
    for (c = 1; c <= b; c++)
    {
        berapa = 0;
        
        cin >> d;
        for (e = 1; e <= 4; e++)
            for (f = 1; f <= 4; f++)
                cin >> a[e][f];
        cin >> g;
         for (e = 1; e <= 4; e++)
            for (f = 1; f <= 4; f++)
                cin >> ah[e][f]; 
        
        for (e = 1; e <= 4; e++)
            for (f = 1; f <= 4; f++)
            {
                if (a[d][e] == ah[g][f])
                {
                    berapa++;
                    apa = a[d][e];
                }    
            }
        
        if (berapa == 0)
           cout << "Case #" << c << ": Volunteer cheated!\n";
        else if (berapa > 1)
             cout << "Case #" << c << ": Bad magician!\n";
        else
            cout  << "Case #" << c << ": " << apa << "\n";
    }
}
