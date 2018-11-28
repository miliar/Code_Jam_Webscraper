#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int ans, ans1, ans2, cnt, cards[4], cards1[4][4], cards2[4][4], i, j, t, temp;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> ans1;
        for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) cin >> cards1[i][j];
        cin >> ans2;
        for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) cin >> cards2[i][j];

        ans = -1; // fetch first answer row
        for (i = 0; i < 4; i++) cards[i] = cards1[ans1 - 1][i];
        for (i = 0; i < 4; i++)
        {
            temp = -1; // search for cards on second answer row
            for(j = 0; j < 4; j++) if (cards2[ans2 - 1][j] == cards[i]) temp = cards[i];
            if (temp != -1) // card found
            {
                if (ans == -1) ans = temp;
                else ans = 999; // bad magician, more than one cards possible
            }
        }

        //display results
        if (ans == -1) cout << "Case #" << cnt << ": Volunteer cheated!" << endl;
        if ((ans >= 1) && (ans <= 16)) cout << "Case #" << cnt << ": " << ans << endl;
        if (ans == 999) cout << "Case #" << cnt << ": Bad magician!" << endl;
    }
    return 0;
}
