/**
 * @file magic_trick.cpp
 *
 * @breif Solving the 'Magic Trick' problem:
 * https://code.google.com/codejam/contest/2974486/dashboard#s=p0
 */
#include <iostream>

using namespace std;

int main()
{
    const int kRowNumber = 4;  // row number of the square
    int test_cases;  // number of test cases
    cin >> test_cases;
    for (int t = 1; t <= test_cases; ++t) {
        int two_rows[2][kRowNumber];  // the two rows the volunteer answered
        int first_row_number;
        // read inputs
        cin >> first_row_number;
        for (int i = 0; i < kRowNumber; ++i) {
            int card = 0;
            for (int j = 0; j < kRowNumber; ++j) {
                cin >> card;
                if (i == first_row_number-1)
                    two_rows[0][j] = card;
            }
        }
        int second_row_number;
        cin >> second_row_number;
        for (int i = 0; i < kRowNumber; ++i) {
            int card = 0;
            for (int j = 0; j < kRowNumber; ++j) {
                cin >> card;
                if (i == second_row_number-1)
                    two_rows[1][j] = card;
            }
        }
        // doing
        int dup_count = 0;   // number of duplicate cards between the two rows
        int dup_card = 0;  // the duplicated card if there is only one
        for (int i = 0; i < kRowNumber; ++i) {
            for (int j = 0; j < kRowNumber; ++j) {
                if (two_rows[0][i] == two_rows[1][j]) {
                    dup_count++;
                    dup_card = two_rows[0][i];
                }
            }
        }
        // output
        cout << "Case #" << t << ": ";
        if (dup_count == 1) {
            cout << dup_card;
        } else if (dup_count == 0) {
            cout << "Volunteer cheated!";
        } else {
            cout << "Bad magician!";
        }
        cout << '\n';
    }
}
