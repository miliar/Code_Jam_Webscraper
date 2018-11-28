#include <iostream>

using namespace std;

void markCards(int *cards)
{
    int row = 0;
    cin >> row;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            int c;
            cin >> c;
            if (i + 1 == row)
                cards[c]++;
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int cards[17] = {0};
        markCards(cards);
        markCards(cards);
        int count = 0;
        int last = 0;
        for (int i = 1; i <= 16; ++i)
        {
            if (cards[i] == 2)
            {
                last = i;
                count++;
            }
        }
        switch (count)
        {
        case 1:
            cout << "Case #" << t << ": " << last << endl;
        break;
        case 0:
            cout << "Case #" << t << ": Volunteer cheated!" << endl;
        break;
        default:
            cout << "Case #" << t << ": Bad magician!" << endl;
        }
    }
    return 0;
}