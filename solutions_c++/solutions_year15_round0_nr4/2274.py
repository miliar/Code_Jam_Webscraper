#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int r, c, x;
        cin >> x >> r >> c;

        bool canLoose = false;

        if(x == 2)
        {
            canLoose = ((r % 2) == 1) && ((c % 2) == 1);
        }

        if(x == 3)
        {
//            bool tmp1 = ((r % 3) == 0) && ((c % 2) == 0);
//            bool tmp1 = ((r % 2) == 0) && ((c % 3) == 0);
            canLoose |= (r == 1) || (c == 1);
//            canLoose |= (r == 4) && (c == 4);
//            canLoose |= (r == 1) && (c == 1);
//            canLoose |= (r == 1) && (c == 2);
//            canLoose |= (r == 2) && (c == 1);
//            canLoose |= (r == 2) && (c == 1);
            canLoose |= !((r == 3) || (c == 3));
        }

        if(x == 4)
        {
            bool ok = false;
            ok |= ((r == 4) && (c == 4));
            ok |= ((r == 3) && (c == 4));
            ok |= ((r == 4) && (c == 3));
                canLoose = !ok;
            }

        if(canLoose)
            cout << "Case #" << t << ": " << "RICHARD" << endl;
        else
            cout << "Case #" << t << ": " << "GABRIEL" << endl;
    }

    return 0;
}
