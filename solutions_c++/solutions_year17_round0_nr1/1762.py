#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i= a; i<= b; i++)
#define FORD(i,a,b) for(int i= a; i>= b; i--)
#define For(i,a,b) for(int i= a; i< b; i++)
#define Ford(i,a,b) for(int i= a; i> b; i--)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define Fill(s,a) memset(s,a,sizeof(s))
#define pb push_back
#define mp make_pair
#define ALL(x) (x).begin(),(x).end()
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef unsigned long long ull;

const int N = 10010;

int n, tests, k, a[N];

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    cin >> tests;
    FOR(t,1,tests)
    {
        string s;
        cin >> s >> k;
        For(i,0,s.length())
            if (s[i] == '-') a[i+1] = 0;
            else a[i+1] = 1;
        n = s.length();
        int res = 0;
        FOR(i,1,n-k+1)
            if (a[i] == 0)
            {
                res++;
                FOR(j,i,i+k-1) a[j] = 1 - a[j];
            }
        FOR(i,1,n)
            if (a[i] == 0) res = -1;
        cout << "Case #" << t << ": ";
        if (res == -1) cout << "IMPOSSIBLE\n";
        else cout << res << endl;
    }
    return 0;
}
