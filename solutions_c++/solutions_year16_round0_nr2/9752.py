#include <iostream>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <string>

using namespace std;

#define LL long long

int main() {
#ifdef _CONSOLE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);
#endif
    
    int t; cin>>t;
    for(int i = 1; i <= t; ++i) {
        string s; cin>>s;
        int ans = 0;
        
        int idx = (int)s.length() - 1;
        while(idx >= 0) {
            if(s[idx] == '-') {
                ans++;
                for(int k = 0; k <= idx; ++k) {
                    if(s[k] == '+') s[k] = '-';
                    else s[k] = '+';
                }
            }
            idx--;
        }
        
        printf("Case #%d: %d\n", i, ans);
        
    }
    
    return 0;
}
