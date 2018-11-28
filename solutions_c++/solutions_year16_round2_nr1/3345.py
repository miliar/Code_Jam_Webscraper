#include <bits/stdc++.h>
using namespace std;

int t;
int c[10];
int m[1000];
string s;

int main()
{
    cin >> t;

    for (int i = 1; i <= t; ++i)
    {
        cin >> s;

        for (char x='A'; x<='Z';++x)
        {
            m[x]=0;
        }

        for (int j = 0; j < 10; ++j)
        {
            c[j] = 0;
        }

        for (int j = 0; j < s.length(); ++j)
        {
            m[s[j]]++;

            if (s[j]=='X')
            {
                c[6]++;
            }
            if (s[j]=='Z')
            {
                c[0]++;
            }
            if (s[j]=='W')
            {
                c[2]++;
            }
            if (s[j] == 'U')
            {
                c[4]++;
            }
            if (s[j]=='G')
            {
                c[8]++;
            }
        }

        c[5] = m['F']-c[4];
        c[7] = m['V']-c[5];
        c[1] = m['O']-c[0]-c[2]-c[4];
        c[3] = m['T']-c[2]-c[8];
        c[9] = m['I']-c[5]-c[6]-c[8];

        cout << "Case #" << i << ": ";

        for (int i = 0; i < 10; ++i)
        {
            for (int j = 0; j < c[i];++j)
            {
                cout<<i;
            }
        }

        cout << endl;
    }
}
