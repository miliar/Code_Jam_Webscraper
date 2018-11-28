#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <utility>
#include <climits>
#include <unordered_set>
#include <set>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        string result;
        result += s[0];
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] >= result[0]) result = s[i] + result;
            else result = result + s[i];
        }
        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}

