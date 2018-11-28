#include <bits/stdc++.h>
using namespace std;

const int N = 110;

char s[N];

int main(){
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas){
        cin >> s;
        int ans = 0;
        char p = s[0];
        for(int i = 1; s[i]; ++i){
            if(p != s[i]) ++ans;
            p = s[i];
        }
        if(p != '+') ++ans;
        cout << "Case #" << cas << ": " << ans << endl;
    }
    return 0;
}