#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("large.in", "r", stdin);
    //freopen("large.out", "w", stdout);
    int nbT;
    cin >> nbT;
    for (int t = 1; t <= nbT; t++)
    {
        cout << "Case #" << t << ": ";

        int D;
        cin >> D;
        vector<int> nbPan(D, 0);

        for (int i = 0; i < D; i++)
            cin >> nbPan[i];
        sort(nbPan.rbegin(), nbPan.rend());
        //cout << nbPan[0] << "vs " << nbPan[1] << endl;
        int deb, fin, mil;
        deb = 0;
        fin = nbPan[0]+1;

        while (fin - deb > 0)
        {
            mil = (deb+fin)/2;
            //cout << mil << "lol" << deb << "==>" << fin<<endl;
            bool isOk = false;


            for (int nbMaxSwap = 0; nbMaxSwap < mil; nbMaxSwap++)
            {
                int nbSwap = 0;
                for (int i = 0; i < D; i++)
                {
                    //int curNbLeft = nbPan[i];
                    nbSwap += nbPan[i]/(mil-nbMaxSwap);
                    if (nbPan[i]%(mil-nbMaxSwap) == 0)
                        nbSwap--;

                }
                if (nbSwap <= nbMaxSwap)
                {
                    isOk = true;
                    break;
                }
            }

            if (isOk)
                fin = mil;
            else
                deb = mil+1;

        }


        cout << deb << '\n';


    }
    return 0;
}
