#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define RREP(i,n) for(int i = (n)-1; i >= 0; i--)
#define FOR(i, l, r) for(int i = l; i < r; i++)
#define RFOR(i, l,r) for(int i= (l)-1; i>= (r) ; i--)

#define int64 int64_t
#define uint64 uint64_t
#define uint unsigned

int t, n;

int solve()
{
    static constexpr int flag = 1023;
    static const int digi[10] = { 1, 2, 4, 8, 16, 32
                                , 64, 128, 256, 512};
    int is = 0, c = 0;
    while(c < 10000 && is != flag)
    {
        c++;
        string s = to_string(n * c);
        REP(i, s.size())
            is = is | digi[s[i] - '0'];
    }
    if(c >= 10000) return -1;
    else return n * c;
}

int main()
{
    cin >> t;
    REP(i, t)
    {
        cin >> n;
        int d = solve();
        cout << "Case #" << i+1 << ": " << (d == -1 ? "INSOMNIA" : to_string(d ) )
            << endl;
    }
}
