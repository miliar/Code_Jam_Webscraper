#include<bits/stdc++.h>
#define ll long long
using namespace std;
const ll nmax = 100005;
const int mod = 1e9 + 7;
const int inf = 1e9;
const long double eps = 1e-9;
const long double PI = acos(-1.0);
vector<int> v;
int main(){
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int q = 1; q <= t; ++q){
        string s;
        cin >> s;
        v.clear();
        v.assign(26, 0);
        vector<int> ans;
        for(int i = 0; i < s.size(); ++i){
            v[s[i] - 'A']++;
        }
        while(v['Z' - 'A']){
            v['Z' - 'A']--;
            v['E' - 'A']--;
            v['R' - 'A']--;
            v['O' - 'A']--;
            ans.push_back(0);
        }
        while(v['W' - 'A']){
            v['T' - 'A']--;
            v['W' - 'A']--;
            v['O' - 'A']--;
            ans.push_back(2);
        }
        while(v['U' - 'A']){
            v['F' - 'A']--;
            v['O' - 'A']--;
            v['U' - 'A']--;
            v['R' - 'A']--;
            ans.push_back(4);
        }
        while(v['X' - 'A']){
            v['S' - 'A']--;
            v['I' - 'A']--;
            v['X' - 'A']--;
            ans.push_back(6);
        }
        while(v['G' - 'A']){
            v['E' - 'A']--;
            v['I' - 'A']--;
            v['G' - 'A']--;
            v['H' - 'A']--;
            v['T' - 'A']--;
            ans.push_back(8);
        }
        while(v['O' - 'A'] && v['N' - 'A'] && v['E' - 'A']){
            v['O' - 'A']--;
            v['N' - 'A']--;
            v['E' - 'A']--;
            ans.push_back(1);
        }
        while(v['F' - 'A'] && v['I' - 'A'] && v['V' - 'A'] && v['E' - 'A']){
            v['F' - 'A']--;
            v['I' - 'A']--;
            v['V' - 'A']--;
            v['E' - 'A']--;
            ans.push_back(5);
        }
        while(v['N' - 'A'] > 1 && v['I' - 'A'] && v['E' - 'A']){
            v['N' - 'A']--;
            v['I' - 'A']--;
            v['N' - 'A']--;
            v['E' - 'A']--;
            ans.push_back(9);
        }
        while(v['S' - 'A'] && v['E' - 'A'] > 1 && v['V' - 'A'] && v['N' - 'A']){
            v['S' - 'A']--;
            v['E' - 'A']--;
            v['V' - 'A']--;
            v['E' - 'A']--;
            v['N' - 'A']--;
            ans.push_back(7);
        }
        while(v['T' - 'A'] && v['H' - 'A'] && v['R' - 'A'] && v['E' - 'A'] > 1){
            v['T' - 'A']--;
            v['H' - 'A']--;
            v['R' - 'A']--;
            v['E' - 'A']--;
            v['E' - 'A']--;
            ans.push_back(3);
        }
        sort(ans.begin(), ans.end());
        cout << "Case #" << q << ": ";
        for(int i = 0; i < ans.size(); ++i) cout << ans[i];
        cout << '\n';
    }
    return 0;
}

