#include <bits/stdc++.h>
using namespace std;

string s;
int t,c;
bool f;

int main()
{
    cin >> t;

    for (int i = 1; i <= t; ++i)
    {
        c = 0;

        cin >> s;
        cout << "Case #" << i << ": ";

        if (s[0] == '-')
        {
            f = false;
        }
        else
        {
            f = true;
        }

        for (int j = 1; j < s.length(); ++j)
        {
            if (s[j] != s[j-1])
            {
                c++;
            }
        }

        if (!f)
        {
            if (c%2==0)
            {
                cout << c+1 << endl;
            }
            else
            {
                cout << c << endl;
            }
        }
        else
        {
            if (c%2==0)
            {
                cout << c << endl;
            }
            else
            {
                cout << c+1 << endl;
            }
        }
    }
}
