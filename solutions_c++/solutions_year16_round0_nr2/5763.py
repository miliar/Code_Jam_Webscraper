#include <iostream>
#include <algorithm>

using namespace std;

char tab[101];

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    freopen("t3in", "r", stdin);
    freopen("t3.out", "w", stdout);

    int nbT;
    cin >> nbT;
    char cv[256];
    cv['-'] = '+';
    cv['+'] = '-';

    for (int t = 1; t <= nbT; t++)
    {
        cin >> tab;
        int rep = 0;
        int len = 0;
        while (tab[len] != 0)
            len++;
        int lastPos = len-1;
        //cout << "len=" << len << endl;

        while (true)
        {
            while (lastPos >= 0 && tab[lastPos] == '+')
                lastPos--;
            if (lastPos == -1)
                break;
            //cout << "lol" <<rep<< endl;


            //cout << tab  << "===>";
           // getchar();
            if (tab[0] != '-')
            {
                rep++;
                int i = 0;
                while (i < len && tab[i] == '+')
                {
                    tab[i] = '-';
                    i++;
                }
                //cout << tab << "======>";
            }
            while (lastPos >= 0 && tab[lastPos] == '+')
                lastPos--;
            if (lastPos == -1)
                break;

            int pos2 = 0;
            while (pos2 <= lastPos)
            {
                tab[pos2] = cv[tab[pos2]];
                pos2++;
            }


            reverse(tab, tab+lastPos+1);
            //cout << tab << endl;
            rep++;
        }



        cout << "Case #" << t << ": ";
        cout << rep << '\n';
    }


    return 0;
}
