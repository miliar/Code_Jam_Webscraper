#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define RREP(i,n) for(int i = (n)-1; i >= 0; i--)
#define FOR(i, l, r) for(int i = l; i < r; i++)
#define RFOR(i, l,r) for(int i= (l)-1; i>= (r) ; i--)

int solve(string s)
{
    int count = 0;
    static constexpr char pm[] = {'-', '+'}; 
    RREP(i, s.size())
    {
        if(s[i] == pm[count%2])
            count++;
    }
    return count;
}

int main()
{
    int t;
    cin >> t;
    FOR(i, 0, t)
    {
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": "
                << solve(s) << '\n';
    }
}

