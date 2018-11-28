#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

void mod(ll &a, ll b)
{
    a %= b;
    if(a < 0) a += b;
}

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

ifstream fin("B.txt");
ofstream fout("B.out");

ll T[1005], Tests, N, P;

ll total(ll n)
{
    ll ret = 0;
    f(i,1,N) ret += (n+T[i])/T[i];
    return ret;
}

ll solve(ll k)
{
    ll p = 0;
    f(i,1,N) p += (k+T[i]-1) / T[i];
    f(i,1,N) if(k % T[i] == 0)
    {
        p++;
        if(p == P) return i;
    }
}

int main()
{
    fin >> Tests;
    f(testie,1,Tests)
    {
        fin >> N >> P;
        f(i,1,N) fin >> T[i];
        ll a = 0, b = 100000000000000000ll;
        while(b-a > 1)
        {
            ll p = (a+b) / 2;
            if(total(p) < P) a = p;
            else b = p;
        }
        if(total(a) == P) fout << "Case #" << testie << ": " << solve(a) << "\n";
        else fout << "Case #" << testie << ": " << solve(b) << "\n";
    }
}
