#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

inline void Normalize(vector<int> &values) {
    vector< pair<int, int> > normalValues;
    for (int i = 0; i < int(values.size()); ++i)
        normalValues.push_back(make_pair(values[i], i));
    sort(normalValues.begin(), normalValues.end());
    for (int i = 0, j = 0; i < int(normalValues.size()); ++i) {
        if (i > 0 && normalValues[i - 1].first != normalValues[i].first)
            ++j;
        values[normalValues[i].second] = j;
    }
}

inline int GetSwaps(vector<int> initial, const vector<int> &final) {
    int n = int(final.size()), swaps = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            if (initial[j] == final[i]) {
                swaps += j - i;
                for (int k = j; k > i; --k)
                    swap(initial[k], initial[k - 1]);
            }
        }
    }
    return swaps;
}

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test) {
        int n;
        cin >> n;
        vector<int> values = vector<int>(n);
        for (int i = 0; i < n; ++i)
            cin >> values[i];
        Normalize(values);
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            int left = 0, right = 0;
            bool found = false;
            for (int j = 0; j < n; ++j) {
                if (values[j] < i)
                    continue;
                if (values[j] == i) {
                    found = true;
                    continue;
                }
                if (!found)
                    ++left;
                else
                    ++right;
            }
            answer += min(left, right);
        }
        cout << "Case #" << test << ": " << answer << "\n";
    }
    cin.close();
    cout.close();
    return 0;
}
