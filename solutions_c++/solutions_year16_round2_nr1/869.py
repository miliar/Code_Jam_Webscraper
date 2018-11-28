#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <map>


using namespace std;




int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        string s;
        cin >> s;
        vector<int> ans;
        vector<int> cnt;
        cnt.resize(26);
        for (int i = 0; i < (int)s.size(); i++) {
            cnt[s[i] - 'A']++; 
        }
        for (int i = 0; i < cnt['G' - 'A']; i++) {
            ans.push_back(8);
            cnt['E' - 'A']--;
            cnt['I' - 'A']--;
            cnt['H' - 'A']--;
            cnt['T' - 'A']--;
        }
        cnt['G' - 'A'] = 0;
        for (int i = 0; i < cnt['X' - 'A']; i++) {
            ans.push_back(6);
            cnt['S' - 'A']--;
            cnt['I' - 'A']--;
        }
        cnt['X' - 'A'] = 0;
        for (int i = 0; i < cnt['S' - 'A']; i++) {
            ans.push_back(7);
            cnt['E' - 'A']--;
            cnt['V' - 'A']--;
            cnt['E' - 'A']--;
            cnt['N' - 'A']--;
        }
        cnt['S' - 'A'] = 0;
        for (int i = 0; i < cnt['V' - 'A']; i++) {
            ans.push_back(5);
            cnt['F' - 'A']--;
            cnt['I' - 'A']--;
            cnt['E' - 'A']--;
        }
        cnt['V' - 'A'] = 0;
        for (int i = 0; i < cnt['F' - 'A']; i++) {
            ans.push_back(4);
            cnt['O' - 'A']--;
            cnt['U' - 'A']--;
            cnt['R' - 'A']--;
        }
        cnt['F' - 'A'] = 0;
        for (int i = 0; i < cnt['W' - 'A']; i++) {
            ans.push_back(2);
            cnt['T' - 'A']--;
            cnt['O' - 'A']--;
        }
        cnt['W' - 'A'] = 0;
        for (int i = 0; i < cnt['I' - 'A']; i++) {
            ans.push_back(9);
            cnt['N' - 'A']--;
            cnt['N' - 'A']--;
            cnt['E' - 'A']--;
        }
        cnt['I' - 'A'] = 0;
        for (int i = 0; i < cnt['N' - 'A']; i++) {
            ans.push_back(1);
            cnt['O' - 'A']--;
            cnt['E' - 'A']--;
        }
        cnt['N' - 'A'] = 0;
        for (int i = 0; i < cnt['O' - 'A']; i++) {
            ans.push_back(0);
            cnt['Z' - 'A']--;
            cnt['E' - 'A']--;
            cnt['R' - 'A']--;
        }
        cnt['O' - 'A'] = 0;
        for (int i = 0; i < cnt['H' - 'A']; i++) {
            ans.push_back(3);
        }
        sort(ans.begin(), ans.end());
        cout << "Case #" << ii + 1 << ": "; 
        for (int i = 0; i < (int)ans.size(); i++) {
            cout << ans[i];
        }
        cout << endl;
    }
    return 0;
}
//"THREE"