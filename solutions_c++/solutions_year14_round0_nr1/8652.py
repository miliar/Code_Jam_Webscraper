#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const int maxN = 4;

int main() {

    int T;
    cin >> T;

    for (int caseNumber = 1; T; --T, ++caseNumber) {

        int row;
        cin >> row;

        int card[maxN][maxN];
        for (int i = 0; i < maxN; ++i)
            for (int j = 0; j < maxN; ++j)
                cin >> card[i][j];

        vector<bool> mark(maxN * maxN, false);
        for (int j = 0; j < maxN; ++j)
            mark[card[row - 1][j] - 1] = true; // cos it 0-indexed

        int _row;
        cin >> _row;

        int _card[maxN][maxN];
        for (int i = 0; i < maxN; ++i)
            for (int j = 0; j < maxN; ++j)
                cin >> _card[i][j];

        int cardsCount = 0;
        int ans;

        for (int j = 0; j < maxN; ++j)
            if (mark[_card[_row - 1][j] - 1]) {
                ++cardsCount;
                ans = _card[_row - 1][j];
            }

        cout << "Case #" << caseNumber << ": ";

        switch (cardsCount) {
            case 1:
                cout << ans << endl;
                break;

            case 0:
                cout << "Volunteer cheated!" << endl;
                break;

            default:
                cout << "Bad magician!" << endl;
                break;
        }

    }

    return 0;

}
