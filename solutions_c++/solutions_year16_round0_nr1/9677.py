#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

void process(unsigned long num, unordered_set<int> &dict) {
    while (num > 0) {
        dict.erase(int(num % 10));
        num /= 10;
    }
}

int main() {
    int T;
    unsigned long N;
    cin >> T;
    vector<unsigned long> results;
    for (int i = 1; i <= T; i++) {
        cin >> N;
        unsigned long result = 0;
        if (N == 0) {
            results.push_back(result);
            continue;
        }
        unordered_set<int> dict;
        for (int j = 0; j <= 9; j++) {
            dict.insert(j);
        }
        for (int j = 1; N * j <= ULONG_MAX; j++) {
            process(N * j, dict);
            if (dict.empty()) {
                result = N * j;
                break;
            }
        }
        results.push_back(result);
    }
    for (int i = 1; i <= T; i++) {
        if (results[i - 1] == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << i << ": " << results[i - 1] << endl;
        }
    }
}