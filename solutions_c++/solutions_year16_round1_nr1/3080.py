#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
   freopen("in.txt", "rt", stdin);
   freopen("out.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 1 ; i <= t ; i++ )
    {
        string S;
        cin >> S;
        int n = int(S.size());
        string res;
        res += S[0];
        for (int j = 1 ; j < n ; j++)
        {
            if (S[j] >= res[0])
                res = S[j] + res;
            else
                res += S[j];
        }
         cout << "Case #" << i << ": " << res << "\n";
    }


}
