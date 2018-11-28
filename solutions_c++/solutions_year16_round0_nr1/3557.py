#include <iostream>
#include<unordered_set>

using namespace std;

class Solution {
public:
    Solution(int n): n(n), k(0) {};
    bool next() {
        if (n == 0) {
            return true;
        }
        k += n;
        process();
        if (s.size() == 10) {
            return true;
        } else {
            return false;
        }
    }

    void process() {
        int p = k;
        while (p != 0) {
            s.insert(p % 10);
            p /= 10;
        }
    }

    string res() {
        return k == 0 ? "INSOMNIA" : to_string(k);
    }

private:
    int n, k;
    unordered_set<int> s;
};

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n;
        cin >> n;
        Solution sol(n);
        while (!sol.next()) {}
        cout << "Case #" << i << ": " << sol.res() << "\n";

    }

    return 0;
}