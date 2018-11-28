#include <iostream>
#include <cstdint>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        uint64_t N;
        unordered_set<char> s{'0','1','2','3','4','5','6','7','8','9'};
        cin >> N;
        cout << "Case #" << t << ": ";
        if (N == 0) { cout << "INSOMNIA" << endl;}
        else {
            uint64_t cnt = 1;
            string curr;
            uint64_t currNum;
            do {
                currNum = N * cnt;
                curr = to_string(currNum);
                for (int j = 0; j < curr.length(); ++j) {
                    s.erase(curr[j]);
                }
                ++cnt;
            } while (!s.empty());
            cout << currNum << endl;
        }
    }
}
