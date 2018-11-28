#include<bits/stdc++.h>
using namespace std;
int i, j, k, l, x, y, z, m, n, ans, p, q, t;

string s;

int main()
{

    freopen("B-large.txt", "r", stdin);
    freopen("B-largeoutput.txt", "w", stdout);

    cin >> t;
    int cs = 1;

    while(t--){

        cin >> s;

        int len = s.size();

        printf("Case #%d: ", cs++);

        if(len == 1){
            if(s[0] == '+') cout << 0 << endl;
            else cout << 1 << endl;
            continue;
        }

        int ans = 0;

        for(i = 1; i < len; i++){

            if(s[i] == s[i - 1]) continue;

            else{
                ans++;
            }

        }
        if(s[len - 1] == '-') ans++;

        cout << ans << endl;

    }


    return 0;
}
