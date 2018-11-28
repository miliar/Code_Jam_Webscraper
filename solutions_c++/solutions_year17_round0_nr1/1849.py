#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
const int INF = ~(1<<31);


int main()
{
    int t;
    cin >> t;
    rep(k,0,t)
    {
        string s;
        int n, moves = 0;
        cin >> s >> n;
        rep(i,0,size(s)-n+1)
        {
            if(s[i] == '-')
            {
                rep(j,0,n) s[i+j] = (s[i+j] == '-' ? '+' : '-');
                moves++;
            }
        }

        bool found = false;
        rep(i,0,size(s))
        {
            if(s[i] == '-') found = true;
        }

        cout << "Case #" << k+1 << ": ";
        if(found) cout << "IMPOSSIBLE";
        else cout << moves;
        cout << endl;
    }
    return 0;
}
