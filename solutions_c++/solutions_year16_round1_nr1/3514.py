#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <deque>
using namespace std;

void solve_case(int test_case) {
    string word;
    cin >> word;
    deque<char> ans;
    ans.push_front(word[0]);
    for (int i = 1; i < word.size(); i++) {
        if (word[i] >= ans.front()) {
            ans.push_front(word[i]);
        } else {
            ans.push_back(word[i]);
        }
    }
    cout << "Case #" << test_case << ": ";
    for (char &ch : ans) {
        cout << ch;
    }
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        solve_case(TC);
    }

    return 0;
}