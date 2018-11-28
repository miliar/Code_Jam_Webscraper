#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    int N = 0;
    while (N < T) {
        N++;
        cout << "Case #" << N << ": ";

        int firstRow;
        cin >> firstRow;
        set<int> firstSet;
        for (int i = 0; i < 4; ++ i) {
            for (int j = 0; j < 4; ++ j) {
                int tmp;
                cin >> tmp;
                if ((i + 1) == firstRow) {
                    firstSet.insert(tmp);
                }
            }
        }
        int secondRow;
        cin >> secondRow;
        set<int> secondSet;
        for (int i = 0; i < 4; ++ i) {
            for (int j = 0; j < 4; ++ j) {
                int tmp;
                cin >> tmp;
                if ((i + 1) == secondRow) {
                    secondSet.insert(tmp);
                }
            }
        }
        vector<int> result(10);
        auto it = set_intersection(firstSet.begin(), firstSet.end(), secondSet.begin(), secondSet.end(), result.begin());
        result.resize(it - result.begin());
        if (result.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (result.size() == 1) {
            cout << result.front() << endl;
        } else {
            cout << "Bad magician!" << endl;
        }
    }
}
