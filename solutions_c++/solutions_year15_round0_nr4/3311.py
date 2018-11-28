#include <bits/stdc++.h>
using namespace std;

int main()
{   
    int TC, x, r, c;
    int k = 1;

    cin >> TC; 

    while(TC--)
    {
        cin >> x >> r >> c;

        cout << "Case #" << k++ << ": ";

        if (c < r) swap(r, c);

        if (c < x)  {cout << "RICHARD" << endl;} // richard chooses a line and wins
        
        else if (x == 1) {cout << "GABRIEL" << endl;} // gabriel always wins

        else if (x == 2)
        {
            if ((r%2 == 0 ) || (c%2 == 0)) {cout << "GABRIEL" << endl;}
            else                           {cout << "RICHARD" << endl;}
        }

        else if(x == 3)
        {
            if ((r == 2 && c == 3) || (r == 3 && c == 3) || (r == 3 && c == 4)) 
            {       
                cout << "GABRIEL" << endl;
            }
            else {cout << "RICHARD" << endl;}
        }
        
        else if (x == 4) 
        {
            if (r > 2) {cout << "GABRIEL" << endl;}
            else       {cout << "RICHARD" << endl;}
        }
    }

    return 0;
}
