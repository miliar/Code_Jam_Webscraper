#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    string s;
    int t, f, a;
    cin >> t;
    for (int i = 1; i <= t; ++i){
        a = 0;
        cin >> s >> f;
        cout << "Case #" << i << ": ";
        for (int j = f-1; j < s.size(); ++j){
            if (s[j-(f-1)] == '-'){
                a++;
                for (int k = 0; k < f; ++k){
                    if (s[j-(f-1)+k] == '-') s[j-(f-1)+k] = '+';
                    else s[j-(f-1)+k] = '-';
                }
            }
        }
        bool check = false;
        for (int j = 0; j < s.size(); ++j){
            if (s[j] == '-'){
                check = true;
                break;
            }
        }
        if (check) cout << "IMPOSSIBLE\n";
        else cout << a << '\n';
    }
}
