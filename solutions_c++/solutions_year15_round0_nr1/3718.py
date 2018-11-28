#include <bits/stdc++.h>
using namespace std;
bool check(vector<int> t) {
    int stand = 0;
    for(int i = 0; i <= t.size(); i++) {
        if(stand < i && t[i] != 0)
            return 0;
        stand += t[i];
    }
    return 1;
}
int main() {
    int t; cin >> t;
    for(int T = 1; T <= t; T++) {
        int n; 
        string s;
        cin >> n >> s;
        vector<int> t;
        for(int i = 0; i <= n; i++) {
            t.push_back(int(s[i] - '0'));
        }
        int ans = 0;
        n = t.size();
        while(!check(t)) {
            n = t.size();/*
            cout << n << " " << t.size() << "\n";
            for(auto a: t) {
                cout << a << " ";
            }cout << "\n";*/
            
            t[n]--;
            t[0]++;
            ans++;
            while(t.back() == 0) {t.pop_back();}
//             for(auto a: t) {
//                 cout << a << " ";
//             }cout << "!!!\n";
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}