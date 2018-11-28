#include <bits/stdc++.h>
using namespace std;

string s;
int n;

bool valid()
{
    for(int i = 0; i < n; i++)
        if(s[i] == '-')
            return false;
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,ans,pos,conv,ntest=1;
    cin >> T;
    while(T--)
    {
        cin >> s;
        n = s.size();
        ans = 0;
        while(!valid())
        {
            for(pos = 1; pos < n; pos++)
                if(s[pos] != s[0])
                    break;
            conv = (s[0] == '-');
            for(int i = 0; i < pos; i++)
                if(conv)
                    s[i] = '+';
                else
                    s[i] = '-';
            ans++;
        }
        cout << "Case #" << ntest++ << ": " << ans << '\n';
    }
    return 0;
}