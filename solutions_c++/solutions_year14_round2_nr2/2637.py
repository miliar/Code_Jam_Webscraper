#include <iostream>
#include <fstream>

using namespace std;

fstream plik;

bool tab[1001];

int main()
{

    plik.open("out.txt");
    int t;
    cin >> t;
    for(int z=1; z<=t; z++)
    {
        int ans = 0;
        int a, b, k;
        cin >> a >> b >> k;

        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                int x = (i&j);
                if(x<k) ans++;
            }
        }
        plik << "Case #" << z <<": "<< ans << "\n";
    }


    return 0;
}
