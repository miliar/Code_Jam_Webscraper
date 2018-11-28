#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t;

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    int test = 0;
    while(t--) {
        int n;
        test += 1;
        cin >> n;

        string s;

        cin >> s;

        int cc = s[0]-'0';

        int ans = 0;

        for(int i = 1; i < s.size(); i++) {
            if(cc >= i) {
                cc += s[i]-'0';
            }
            else {
                ans += (i-cc);
                cc = i + s[i]-'0';
            }
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
}
