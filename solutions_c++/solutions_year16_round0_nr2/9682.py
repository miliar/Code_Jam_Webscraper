#include <bits/stdc++.h>

#define ull unsigned long long

using namespace std;

const int MAXN = 1e6 + 5;

void task(string s, int t){
    cout << "Case #" << t << ": ";
    int n = s.length();
    vector <pair<int, int> > dp(n + 1, pair<int, int> (0, 0));
    for (int i = 0; i < n; i++){
        int ind = i + 1;
        if (s[i] == '-'){
            dp[ind].first = dp[ind - 1].second + 1;
            dp[ind].second = dp[ind - 1].second;
        }
        else {
            dp[ind].second = dp[ind - 1].first + 1;
            dp[ind].first = dp[ind - 1].first;
        }
    }
    cout << dp[n].first << endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    string s;
    cin >> T;
    for (int t = 0; t < T; t++){
        cin >> s;
        task(s, t + 1);
    }
    return 0;
}
