#include<bits/stdc++.h>
#define all(a) a.begin(), a.end()
#define int long long
int inf = 1e12;
using namespace std;


signed main(int argc, char *argv[])
{
    freopen("A-large.in", "r", stdin);
     freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int q = 1; q <= T; q++)
    {
        int S;
        cin >> S;
        string s;
        cin >> s;
        vector<int> a(S + 1);
        for(int i = 0; i < s.size(); i++)
            a[i] = s[i] - '0';
        int st = a[0];
        int ans = 0;
        for(int i = 1; i < a.size(); i++)
            if(st >= i)
                st += a[i];
            else
            {
                ans += i - st;
                st = i + a[i];
            }
        cout << "Case #" << q << ": " << ans << '\n';
    }
    return 0;
}
