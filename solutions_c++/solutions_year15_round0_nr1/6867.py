#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long int t, i;
    cin >> t;
    for(i = 1; i <= t; i++){
        unsigned long long  n, ans = 0, cnt = 0;
        string s;
        cin >> n >> s;
        for(long int i = 0; i < s.size(); i++){
            if(ans >= i){
                ans += (s[i] - 48);
            }
            else{
                cnt += i - ans;
                ans = i + (s[i] - 48);
            }
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}
