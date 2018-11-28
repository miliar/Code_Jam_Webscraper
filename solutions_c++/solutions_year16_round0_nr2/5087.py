#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string s;
    int ans = 0;
    for(int i = 0;i < n;i++){
        ans = 0;
        cin >> s;
        int j = 0;
        if(s[0] == '-'){
            ans++;
            while(s[j] == '-') j++;
        }
        for(;j < s.size();j++){
            if(s[j] == '-'){
                ans += 2;
                while(s[j] == '-') j++;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
