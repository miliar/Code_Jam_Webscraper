#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        int n,now(0),ans(0);
        string s;
        cin >> n >> s;
        for(int i = 0; i < n + 1; ++i) {
            int  t = max(0,i - now);
            now += s[i] - '0' + t;
            ans += t;
        }
        cout << "Case #" <<  cas << ": " << ans << endl;         
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
} 
