#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++)
    {
        cout << "Case #" << tc + 1 << ": ";

        int s;
        string line;
        cin >> s >> line;

        int cur = 0;
        int ans = 0;

        for (int i = 0; i < line.length(); i++)
        {
            if (cur < i)
                ans += i - cur, cur = i;
            cur += line[i] - '0';
        }

        cout << ans << endl;

    }

    return 0;
}
