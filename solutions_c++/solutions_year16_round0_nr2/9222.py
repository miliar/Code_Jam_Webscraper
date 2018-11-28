#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int T;
string str;
int solution;
vector<char> v;

int main() {
    cin >> T;
    getline(cin, str);
    for (int test = 1; test <= T; ++test) {
        getline(cin, str);
        v.clear();
        for (size_t i = 0; i < str.length(); ++i)
            v.push_back(str[i]);
        vector<char>::iterator it;
        it = unique(v.begin(), v.end());
        v.resize( distance(v.begin(), it) );
        solution = v.size();
        if (v[v.size() - 1] == '+')
            --solution;
        cout << "Case #" << test << ": " << solution << '\n';
    }
    return 0;
}
