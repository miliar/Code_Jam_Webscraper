#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <fstream>

using namespace std;


int main() {
    fstream cin("/Users/Roman/Desktop/GCJ/input.txt");
    fstream cout("/Users/Roman/Desktop/GCJ/output.txt");
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(18);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        string s;
        cin >> s;
        while (s.length() != 0) {
            if (s.back() == '+') {
                s.pop_back();
            } else {
                break;
            }
        }
        char last = '?';
        int num = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != last) {
                num++;
            }
            last = s[i];
        }
        cout << "Case #" << tt + 1 << ": " << num << "\n";
    }
    return 0;
}