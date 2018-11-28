#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        auto cards = array<bool, 17>();
        int row1;
        cin >> row1;

        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                int val;
                cin >> val;
                if (i == row1)
                {
                    cards[val] = true;
                }
            }
        }

        int row2;
        cin >> row2;
        int countPossible = 0;
        int rightCard = 0;

        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                int val;
                cin >> val;
                if (i == row2)
                {
                    cards[val] = (cards[val] && true);
                    if (cards[val])
                    {
                        ++countPossible;
                        rightCard = val;
                    }
                }
            }
        }

        cout << "Case #" << t << ": ";

        if (countPossible == 1)
        {
            cout << rightCard;
        }
        else if (countPossible == 0)
        {
            cout << "Volunteer cheated!";
        }
        else
        {
            cout << "Bad magician!";
        }
        cout << endl;
    }

    return 0;
}
