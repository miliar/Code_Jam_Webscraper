#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("stuff.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, x, r, c, buf, g = 0;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        cin >> x >> r >> c;
        g = 3;
        if(r > c)
        {
            buf = r;
            r = c;
            c = buf;
        }
        if(x == 1)
            g = 1;
        else if(x == 2)
        {
            if(r*c % 2 == 1)
                g = 2;
            else
                g = 1;
        }
        else if(x == 3)
        {
            if((r * c) % 3 != 0)
                g = 2;
            else
            {
                if(r == 1 && c == 3)
                    g = 2;
                else if(r == 2 && c == 3)
                    g = 1;
                else if(r == 3 && c == 3)
                    g = 1;
                else if(r == 3 && c == 4)
                    g = 1;
            }
        }
        else if(x == 4)
        {
            if((r * c) % 4 != 0)
                g = 2;
            else
            {
                if(r == 1 && c == 4)
                    g = 2;
                else if(r == 2 && c == 2)
                    g = 2;
                else if(r == 2 && c == 4)
                    g = 2;
                else if(r == 3 && c == 4)
                    g = 1;
                else if(r == 4 && c == 4)
                    g = 1;
            }
        }
        if(r * c >= x)
        {
            if(g == 1)
                cout << "Case #" << i << ": GABRIEL";
            else if (g == 2)
                cout << "Case #" << i << ": RICHARD";
        }
        else if (g != 3)
            cout << "Case #" << i << ": RICHARD";
        cout << endl;
    }
    return 0;
}
