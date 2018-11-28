#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>

using namespace std;

int main()
{
    int n_cases = 0;
    cin >> n_cases;
    for (int i = 0; i < n_cases; ++i) {
        int answers[2];
        set<int> lines[4][2];
        for (int k = 0; k < 2; ++k) {
            cin >> answers[k];

            for (int j = 0; j < 4; ++j) {
                copy_n(istream_iterator<int>(cin),
                       4,
                       insert_iterator<set<int>>(lines[j][k], lines[j][k].end()));
            }
        }

        set<int> candidates;
        set_intersection(lines[answers[0] - 1][0].begin(), lines[answers[0] - 1][0].end(),
                         lines[answers[1] - 1][1].begin(), lines[answers[1] - 1][1].end(),
                         inserter(candidates, candidates.end()));

        cout << "Case #" << i + 1 << ": ";
        switch (candidates.size()) {
        case 0:
            cout << "Volunteer cheated!" << endl;
            break;
        case 1:
            cout << *candidates.cbegin() << endl;
            break;
        default:
            cout << "Bad magician!" << endl;
            break;
        }
    }

    return 0;
}