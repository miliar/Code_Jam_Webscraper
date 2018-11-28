
#include <algorithm>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>

#include <stdio.h>
#include <string.h>

using namespace std;

void read_cards(array<array<int, 4>, 4>& cards)
{
    int i, j;
    for (i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
            cin >> cards[i][j];
}

int main()
{
    int i, j, T, row, count, answer;
    set<int> candidates;
    array<array<int, 4>, 4> cards;

    cin >> T;
    for(i = 1; i <= T; i++)
    {
        cin >> row;
        --row;
        read_cards(cards);
        for (j = 0; j < 4; j++)
            candidates.insert(cards[row][j]);
        cin >> row;
        --row;
        read_cards(cards);
        count = 0;
        for (j = 0; j < 4; j++)
            if (candidates.find(cards[row][j]) != candidates.end())
            {
                count++;
                answer = cards[row][j];
            }
        switch (count)
        {
        case 0:
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
            break;
        case 1:
            cout << "Case #" << i << ": " << answer << endl;
            break;
        default:
            cout << "Case #" << i << ": Bad magician!" << endl;
        }
        candidates.clear();
    }
}

