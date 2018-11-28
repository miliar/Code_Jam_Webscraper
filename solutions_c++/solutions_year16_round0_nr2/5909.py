#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>

using namespace std;

inline string flip(const string& s, size_t top) {
        string t {s};
        for(size_t i {0}, j {top - 1}; i < top; ++i, --j) {
                t[i] = (s[j] == '+' ? '-' : '+');
        }
        return t;
}

unordered_map<string, int> precompute() {
        const size_t max_length {10};
        unordered_map<string, int> res;
        for (size_t len {1}; len <= max_length; ++len) {
                string str(len, '+');
                res.emplace(str, 0);
                queue<pair<string, int>> q;
                q.push({str, 0});
                while (!q.empty()) {
                        string s {q.front().first};
                        int k {q.front().second};
                        q.pop();
                        for (size_t i {1}; i <= len; ++i) {
                                string t {flip(s, i)};
                                if (res.find(t) == res.end()) {
                                        res.emplace(t, k + 1);
                                        q.push({t, k + 1});
                                }
                        }
                }
        }
        return res;
}

int main() {
        auto res {precompute()};
        size_t T;
        cin >> T;
        for (size_t i {1}; i <= T; ++i) {
                string cake;
                cin >> cake;
                cout << "Case #" << i << ": " << res.at(cake) << '\n';
        }
        return 0;
}