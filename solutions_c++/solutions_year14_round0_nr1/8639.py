#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <map>
#include <cassert>

using namespace std;

int main() {

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, ans1, ans2;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        vector <vector <int> > first_cards(4, vector<int>(4, 0));
        vector <vector <int> > second_cards(4, vector<int>(4, 0));
        cin >> ans1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> first_cards[i][j];
            }
        }

        cin >> ans2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> second_cards[i][j];
            }
        }

        vector <int> result;
        std::sort(first_cards[ans1 - 1].begin(), first_cards[ans1 - 1].end());
        std::sort(second_cards[ans2 - 1].begin(), second_cards[ans2 - 1].end());
        std::set_intersection(first_cards[ans1 - 1].begin(), first_cards[ans1 - 1].end(), second_cards[ans2 - 1].begin(), second_cards[ans2 - 1].end(), std::back_inserter(result));
        if (result.size() == 0) {
            cout << "Case #" << t + 1 << ": Volunteer cheated!" << endl;
        } else if (result.size() == 1) {
            cout << "Case #" << t + 1 << ": " << result[0] << endl;
        } else if (result.size() > 1) {
            cout << "Case #" << t + 1 << ": Bad magician!" << endl;
        }
        
    }

    return 0;
}