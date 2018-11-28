#include <bits/stdc++.h>

using namespace std;


int main()
{
    int t;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        int tam = s.size();
        bool done = false;
        int res = 0;
        while (!done)
        {
            done = true;
            for (int j = 0; j < tam; j++)
            {
                if (s[j] == '-')
                {
                    if (j > 0)
                        for (int k = 0; s[k] == '+'; k++) s[k] = '-';
                    else
                        for (int k = 0; s[k] == '-'; k++) s[k] = '+';
                    res++;
                    done = false;
                    break;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " <<  res << endl;
    }
}
