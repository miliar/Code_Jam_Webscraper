#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);
    int nbTest;
    cin >> nbTest;

    for(int iTest = 0;iTest < nbTest;iTest++)
    {
        int maxTimid;
        cin >> maxTimid;

        string nombres;
        cin >> nombres;

        int tot = 0;
        int invite = 0;
        for(int iTimid = 0;iTimid < (int)nombres.size();iTimid++)
        {
            if(nombres[iTimid] != '0' && tot + invite < iTimid)
                invite += iTimid - tot;
            tot += nombres[iTimid] - '0';
        }
        cout << "Case #" << iTest + 1 << ": " << invite << endl;
    }
    return 0;
}
