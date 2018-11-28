#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        int grid1[17], grid2[17];
        int guess1, guess2;
        cin >> guess1;
        for (int i = 0; i < 16; ++i)
        {
            int t;
            cin >> t;
            grid1[t] = i / 4;
        }
        cin >> guess2;
        for (int i = 0; i < 16; ++i)
        {
            int t;
            cin >> t;
            grid2[t] = i / 4;
        }
        int match = 0, ans = -1;
        for (int x = 1; x <= 16; ++x)
        {
            if (grid1[x] == guess1 - 1 && grid2[x] == guess2 - 1)
            {
                ++match;
                ans = x;
            }
        }
        if (match == 1)
            cout << "Case #" << cs << ": " << ans << endl;
        else if (match == 0)
            cout << "Case #" << cs << ": Volunteer cheated!" << endl;
        else
            cout << "Case #" << cs << ": Bad magician!" << endl;
    }
}
