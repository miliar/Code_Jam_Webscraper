#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        set<int> sets[2];
        for (int i = 0; i < 2; ++i) {
            int row;
            cin >> row;
            vector<vector<int>> cards(4, vector<int>(4));
            for (int j = 0; j < 4; ++j) {
                for (int k = 0; k < 4; ++k) {
                    cin >> cards[j][k];
                }
            }
            copy(cards[row - 1].begin(), cards[row - 1].end(), inserter(sets[i], sets[i].begin()));
        }
        vector<int> result;
        set_intersection(sets[0].begin(), sets[0].end(), sets[1].begin(), sets[1].end(), back_inserter(result));

        cout << "Case #" << test << ": ";
        if (result.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (result.size() > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << result[0] << endl;
        }
    }
}
