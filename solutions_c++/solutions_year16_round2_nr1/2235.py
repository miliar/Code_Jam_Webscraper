#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i) {
        string s;
        cin >> s;
        vector<int> V(26,0);
        vector<int> ans;
        for (int j=0; j<s.size(); ++j) {
            char c=s[j];
            V[c-'A']++;
        }
        while (V['Z'-'A'] && V['E'-'A'] && V['R'-'A'] && V['O'-'A']) {
            ans.push_back(0);
            V['Z'-'A']--,  V['E'-'A']--, V['R'-'A']--, V['O'-'A']--;
        }
        while (V['E'-'A'] && V['I'-'A'] && V['G'-'A'] && V['H'-'A'] && V['T'-'A']) {
            ans.push_back(8);
            V['E'-'A']--,  V['I'-'A']--, V['G'-'A']--, V['H'-'A']--, V['T'-'A']--;
        }
        while (V['O'-'A'] && V['T'-'A'] && V['W'-'A']) {
            ans.push_back(2);
            V['O'-'A']--,  V['T'-'A']--, V['W'-'A']--;
        }
        while (V['H'-'A'] && V['T'-'A'] && V['R'-'A'] && V['E'-'A'] > 1) {
            ans.push_back(3);
            V['H'-'A']--,  V['T'-'A']--, V['R'-'A']--, V['E'-'A']-=2;
        }
        while (V['F'-'A'] && V['O'-'A'] && V['U'-'A'] && V['R'-'A']) {
            ans.push_back(4);
            V['F'-'A']--,  V['O'-'A']--, V['U'-'A']--, V['R'-'A']--;
        }
        while (V['S'-'A'] && V['I'-'A'] && V['X'-'A']) {
            ans.push_back(6);
            V['S'-'A']--,  V['I'-'A']--, V['X'-'A']--;
        }
        while (V['S'-'A'] && V['V'-'A'] && V['N'-'A'] && V['E'-'A'] > 1) {
            ans.push_back(7);
            V['S'-'A']--,  V['V'-'A']--, V['N'-'A']--, V['E'-'A']-=2;
        }
        while (V['F'-'A'] && V['I'-'A'] && V['V'-'A'] && V['E'-'A']) {
            ans.push_back(5);
            V['F'-'A']--,  V['I'-'A']--, V['V'-'A']--, V['E'-'A']--;
        }
        while (V['E'-'A'] && V['I'-'A'] && V['N'-'A'] > 1) {
            ans.push_back(9);
            V['N'-'A']-=2,  V['I'-'A']--, V['E'-'A']--;
        }
        while (V['O'-'A'] && V['N'-'A'] && V['E'-'A']) {
            ans.push_back(1);
            V['O'-'A']--,  V['N'-'A']--, V['E'-'A']--;
        }
        sort(ans.begin(), ans.end());
        cout << "Case #" << i << ": ";
        for (auto i : ans)
            cout << i;
        cout << endl;


        int sum=0;
        for (auto j : V)
            sum += j;
        assert(!sum);
    }

    return 0;
}
