#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

unordered_set<int> load_data(int n) {
    unordered_set<int> set;
    int data;

    for (int i = 0; i < 16; i++) {
        cin >> data;
        if (i >= (n - 1) * 4 && i < n * 4) {
            set.insert(data);
        }
    }

    return set;
}

int compare(unordered_set<int>& set1, unordered_set<int>& set2) {
    vector<int> result;

    for (auto it = set1.begin(); it != set1.end(); ++it) {
        if (set2.find(*it) != set2.end()) {
            result.push_back(*it);
        }
    }

    if (result.size() == 0) {
        return -2;
    }
    else if (result.size() == 1) {
        return result[0];
    }
    else {
        return -1;
    }
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        int row1, row2;
        cin >> row1;
        unordered_set<int> set1 = load_data(row1);
        cin >> row2;
        unordered_set<int> set2 = load_data(row2);
        int result = compare(set1, set2);

        cout << "Case #" << t << ": ";
        if (result > 0) {
            cout << result << endl;
        }
        else if (result == -2) {
            cout << "Volunteer cheated!" << endl;
        }
        else {
            cout << "Bad magician!" << endl;
        }
    }
}
