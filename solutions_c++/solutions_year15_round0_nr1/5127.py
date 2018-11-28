#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test)
    {
        int smax;
        cin >> smax;

        string s;
        cin >> s;

        int up = (s[0] - '0');
        int invited = 0;

        for (int i = 1; i <= smax; i++)
        {
            if (up < i)
            {
                invited += (i - up);
                up = i;
            }

            up += (s[i] - '0');
        }

        cout << "Case #" << test << ": " << invited << endl;
    }

    return 0;
}

