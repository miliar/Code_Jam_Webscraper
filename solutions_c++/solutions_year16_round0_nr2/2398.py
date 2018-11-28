#include <iostream>
#include <string>

using namespace std;

typedef long long LL;

LL solve(string s){
    s += '+';
    LL cnt = 0;
    for(int i = 0; i+1 < s.size(); ++i){
        if(s[i] != s[i+1]) cnt++;
    }
    return cnt;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        string s;
        cin >> s;
        LL ans = solve(s);
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

