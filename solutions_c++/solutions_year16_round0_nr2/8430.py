#include <bits/stdc++.h>
#define filename "B-large.in"
using namespace std;

const int N = 1e6+10;



int main(){
    freopen(filename,"r", stdin);
    freopen("output.txt", "w", stdout);

    int test, ans;
    string tmp, s;
    cin >> test;
    for(int i = 1; i <= test; ++i){
        ans = 0;
        s.clear();
        cin >> tmp;
        s += tmp[0];
        for(int j = 1, p = 1; j < tmp.length(); ++j){
            if(tmp[j] != s[p-1]) s += tmp[j], p++;
        }
        int sp = 0;
        if(s[0] == '-') ans++, sp = 1;
        for(; sp < s.length(); ++sp) ans += 2 * (s[sp] == '-');
        cout  << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}