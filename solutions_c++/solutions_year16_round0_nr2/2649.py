#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "B.in"
#define FILEOUT "B.out"



int main() {
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_) {
        // Output answer
        string s;
        cin >> s;
        vector<char> numbers;
        char last_sign = 's';
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != last_sign) {
                // cout << i << endl;
                numbers.push_back(s[i]);
                last_sign = s[i];
            }
        }
        // std::reverse(numbers.begin(), numbers.end());
        // char current_sign = ;
        // int count = 0;


        cout << "Case #" << _ << ": ";

        if (last_sign == '+') {
            cout << numbers.size() - 1;
        } else {
            cout << numbers.size();
        }
        cout << "\n";
    }
    return 0;
}
