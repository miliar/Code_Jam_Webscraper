#include <bits/stdc++.h>


using namespace std;


int main()
{
    int tests;
    cin >> tests;
    for (int k = 0; k < tests; ++k)
    {
        string ciag;
        cin >> ciag;
        int grupy = 0;
        for (int i = 0; i < ciag.length(); ++i)
        {
            if (ciag[i] == '+')
                continue;
            else
            {
                ++grupy;
                while (ciag[i] != '+' && i < ciag.length() - 1)
                    ++i;
            }
        }
        if (ciag[0] == '-')
            cout << "Case #" << k+1 << ": " << 2 * grupy - 1 << endl;
        else
              cout << "Case #" << k+1 << ": " << 2 * grupy << endl;
    }
}
