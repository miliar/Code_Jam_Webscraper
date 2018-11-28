#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    char s[1002];

    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int mx;

        cin >> mx;

        cin >> s;

        int count = 0;

        int need = 0;

        for (int j = 0; j <= mx; j++)
        {
            int sub = j - count;
            if (s[j] - '0' > 0 && sub > 0)
            {
                need += sub;
                count += sub;
            }
            count += s[j] - '0';
        }

        cout << "Case #" << i + 1 << ": " << need << endl;
    }
}
