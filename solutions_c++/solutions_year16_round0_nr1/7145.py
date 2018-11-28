#include "junction.h"
#include <set>

void sheep (){
    int N, D, iModhold, Dorig;

    cin >> N;

    for (int i=0; i< N; i++)
    {
        set <int> DList;
        cin >> D;
        Dorig = D;

        while (DList.size() !=10 && D !=0)
        {
//            cout << "DLIST SIZE: " << DList.size() << endl << "D: " << D << endl;
            iModhold =D;
            while (iModhold!=0)
            {
                DList.insert (iModhold%10);
                iModhold = (iModhold - (iModhold%10))/10;
            }
            D=D+Dorig;
        }
        if (D==0) cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        else {
            cout << "Case #" << i+1 << ": " << D-Dorig << endl;
        }
    }


}
