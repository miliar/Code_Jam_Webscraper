#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
    int cards[4][4];
    set<int> s1;
    set<int> s2;
    set<int> result;

    int T;
    cin >> T;

    int row;
    for (int n = 0; n < T; ++n) {
        s1.clear();
        s2.clear();
        result.clear();
        cin >> row;
//        cout << row << "\n";
        row = row - 1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> cards[i][j];
            }
        }
        s1.insert(&(cards[row][0]), &(cards[row][4]));

        cin >> row;
//        cout << row << "\n";
        row = row - 1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> cards[i][j];
            }
        }
        s2.insert(&(cards[row][0]), &(cards[row][4]));


//        for (auto it = s1.begin(); it != s1.end(); ++it) {
//            cout << *it << " ";
//        }
//        cout << "\n";

//        for (auto it = s2.begin(); it != s2.end(); ++it) {
//            cout << *it << " ";
//        }
//        cout << "\n";

        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(result, result.begin()));

//        for (auto it = result.begin(); it != result.end(); ++it) {
//            cout << *it << " ";
//        }
//        cout << "\n";

        cout << "Case #" << n + 1 << ": ";
        if (result.size() > 1) {
            cout << "Bad magician!";
        } else if (result.size() == 1) {
            cout << *(result.begin());
        } else if (result.empty()) {
            cout << "Volunteer cheated!";
        }
        cout << "\n";
    }
    return 0;
}

