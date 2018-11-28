// the glory is for GOD

#include <bits/stdc++.h>

#define DB(x) cerr << __LINE__ << ": " << #x << " = " << (x) << endl;

using namespace std;

int t, n, ans;

string str;

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);    
    
    cin >> t;

    for (int tn = 1; tn <= t; ++tn)
    {
        cin >> n >> str;
        ans = 0;
        int curr = 0;

        for (int i = 0; i < str.size(); ++i)
        {
            int val = str[i] - '0';

            if (val != 0 && curr < i)
            {
                int toAdd = i - curr;
                ans += toAdd;
                curr += toAdd;
            }

            curr += val;
        }

        cout << "Case #" << tn << ": " << ans << endl;
    }
    return 0;
}