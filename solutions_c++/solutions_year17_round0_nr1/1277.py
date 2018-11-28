#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int T, K;
string s;

bool check(){
    for (int i = 0; i < s.size(); ++i){
        if (s[i] == '-'){
            return false;
        }
    }
    return true;
}

void swap(int p){
    for (int i = p; i < p + K; ++i){
        if (s[i] == '+'){
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
}

int solve(){
    int ans = 0;
    for (int i = 0; i <= s.size() - K; ++i){
        if (s[i] == '-'){
            swap(i);
            ans ++;
        }
    }
    if (check()){
        return ans;
    }
    return -1;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t){
        cin >> s >> K;
        cout << "Case #" << t << ": ";
        int ans = solve();
        if (ans == -1){
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}