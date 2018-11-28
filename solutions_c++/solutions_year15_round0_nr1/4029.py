#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cout << "Case #" << z << ": ";
        int smax;
        string s;
        cin >> smax >> s;
        int needed = 0;
        int up = 0;
        for (int i = 0; i <= smax; ++i)
        {
            if (s[i] != '0')
            {
                if (up < i)
                {
                    needed += (i - up);
                    up = i;
                }
                up += (s[i] - '0');
            }
        }
        cout << needed << "\n";
    }
    return 0;
}