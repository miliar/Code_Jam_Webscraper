#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        vector<bool> check(16, false);
        int card[4][4];
        int one, two;
        int ans_num = 0, ans_card = 0;

        cin >> one;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> card[i][j];

        --one;
        for (int j = 0; j < 4; ++j)
            check[card[one][j] - 1] = true;

        cin >> two;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> card[i][j];

        --two;
        for (int j = 0; j < 4; ++j) {
            if (check[card[two][j] - 1]) {
                ++ans_num;
                ans_card = card[two][j];
            }
        }

        cout << "Case #" << t << ": ";
        if (ans_num == 0)
            cout << "Volunteer cheated!\n";
        else if (ans_num == 1)
            cout << ans_card << "\n";
        else
            cout << "Bad magician!\n";
    }

    return 0;
}
