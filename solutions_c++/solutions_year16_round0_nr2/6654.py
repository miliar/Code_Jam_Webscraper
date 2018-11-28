#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T, n;
    int ans;
    string s;
    cin >> T;
    for(int t=1;t<=T;++t)
    {
        cin >> s;
        n = s.length();
        ans = 0;
        for(int i=n-1; i>=0; --i)
        {
            if(s[i] == '-')
            {
                int j;
                for(j=0; j<=i; ++j)
                    if(s[j] == '-')
                        break;
                ans += (j != 0);
                for(;j<=i;++j)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                reverse(s.begin(),s.begin()+i+1);
                ans++;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

