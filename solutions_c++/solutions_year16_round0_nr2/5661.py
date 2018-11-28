#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ifstream cin("B-large.in.txt");
    ofstream cout("B-large.out.txt");
    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q) {
        string s;
        cin >> s;
        
        char last = '1';
        int len = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != last) {
                last = s[i];
                ++len;
            }
        }
        
        
        cout <<  "Case #" << q << ": " << len - (last == '+') << "\n";
    }
}
