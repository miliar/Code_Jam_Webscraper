#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    string s, w;

    for(int i = 1; i <= T; ++i)
    {
        cin >> s;
        w = s[0];

        for(int j = 1; j < s.length(); ++j)
        {
            if (w[0] <= s[j])
            {
                w = s[j] + w;
            }
            else
            {
                w = w + s[j];
            }
        }

        cout << "Case #" << i << ": " << w << endl;
    }

    return 0;
}
