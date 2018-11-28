#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;

        int ad = 0;
        int cu = 0;
        for(int i = 0; i <= n; ++i)
        {
            int x = s[i] - '0';
            while(cu < i)
            {
                ++cu;
                ++ad;
            }
            cu += x;
        }
        cout << "Case #" << t << ": " << ad << endl;
    }

    return 0;
}
