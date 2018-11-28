#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

string s;
int k;

void solve(){
    cin >> k;
    cin >> s;

    int cur = 0, res = 0;
    for (int i = 0; i <= k; i++){
        if (cur < i){
            res += i-cur;
            cur = i;
        }
        cur += (s[i]-'0');
    }
    cout << res << endl;

}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }

    return 0;
}
