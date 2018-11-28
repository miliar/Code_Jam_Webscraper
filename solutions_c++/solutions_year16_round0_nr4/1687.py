#include <iostream>
#include <string>
#include <climits>

using namespace std;

int main()
{
    int t, k, c, s;
    cin >> t;
    for (int a=1; a<=t; a++)
    {
        cin >> k;
        cin >> c;
        cin >> s;
        cout << "CASE #" << a << ": ";
        /*if (k-(c-1)-s>0)
        {
            cout << "IMPOSSIBLE";
        }
        else if (c == 1)
        {
            for (int i=1; i<=k; i++)
            {
                cout << i << " ";
            }
        }
        else
        {
            for (int i=0; i<s && i<; i++)
            {
                cout << (c-1+i)*k << " ";
            }
        }*/
        if (c == 1)
        {
            for (int i=1; i<=k; i++)
            {
                cout << i << " ";
            }
        }
        else {
            for (int i=1; i<=s && i<=k ; i++)
            {
                cout << i*k << " ";
            }
        }
        cout << endl;
    }

    return 0;
}

