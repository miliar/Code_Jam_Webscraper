// https://code.google.com/codejam/contest/2974486/dashboard
#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <string>
#include <set>
#include <vector>

using namespace std;

const int NUM_COLS = 4;
const int NUM_ROWS = 4;

namespace {

void getRow(set<int> *row) {
    for (int i = 0; i < NUM_COLS; ++i) {
        int val;
        cin >> val;
        if (row) {
            row->insert(val);
        }
    }
}


}
int main()
{
    int numTests;
    cin >> numTests;
    for (int test = 0; test < numTests; ++test)
    {
        const int NUM_COLS = 4;
        int row1,row2;
        set<int> row_val1;
        set<int> row_val2;

        cin >> row1;
        for (int i = 0; i < row1; ++i) {
            row_val1.clear();
            getRow(&row_val1);
        }
        for (int i = row1; i < NUM_ROWS; ++i) {
            getRow(0);
        }
        cin >> row2;
        for (int i = 0; i < row2; ++i) {
            row_val2.clear();
            getRow(&row_val2);
        }
        for (int i = row2; i < NUM_ROWS; ++i) {
            getRow(0);
        }

        set<int> cards;
        set_intersection(row_val1.begin(), row_val1.end(),
                         row_val2.begin(), row_val2.end(),
                         inserter(cards, cards.begin()));
        cout << "Case #" << test + 1 << ": ";
        if (cards.empty()) {
            cout << "Volunteer cheated!" << endl;
        }
        else if (cards.size() == 1) {
            cout << *cards.begin() << endl;
        }
        else {
            cout << "Bad magician!" << endl;
        }
     }
    return 0;
}
