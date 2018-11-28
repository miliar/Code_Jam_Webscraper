#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;
int t , k;
string s;
int main(){
    freopen("1.in" , "r" , stdin);
    freopen("1.out" , "w" , stdout);
    cin >> t;
    for (int cas = 1; cas <= t; ++ cas)
    {
        cin >> k;
        cin >> s;
        int ans = 0;
        int now = s[0] -'0';
        for ( int i = 1; i < s.size(); ++ i)
            if (s[i] > '0'){
                    ans = max(ans , i - now);
                    now += s[i] - '0';
            }
         printf("Case #%d: %d\n" , cas , ans);
    }
}
