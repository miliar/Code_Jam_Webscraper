#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int k=1; k<=t; k++)
    {
        int x, r, c;
        cin >> x >> r >> c;

        cout << "Case #" << k << ": ";

        if(x == 1)
            cout << "GABRIEL\n";
        if(x == 2)
        {
            if((r==1 && c==1) || r*c%2 == 1)
                cout << "RICHARD\n";
            else
                cout <<  "GABRIEL\n";
        }
        if(x == 3)
        {
            if((c*r%3 == 0) && (c*r > 3))
                cout << "GABRIEL\n";
            else
                cout << "RICHARD\n";
        }
        if(x == 4)
        {
            if((c == 4 && r == 4) || (c*r == 12))
                cout << "GABRIEL\n";
            else
                cout << "RICHARD\n";
        }
    }

    return 0;
}
