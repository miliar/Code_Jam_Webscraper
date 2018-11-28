#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------

int T;
ll N;

ifstream fin("A.TXT");
ofstream fout("A.OUT");

ll rev(ll n)
{
    string s;
    while(n)
    {
        s += (char) (n%10 + '0');
        n /= 10;
    }

    ll ret = 0;
    for(char c : s)
    {
        ll d = c - '0';
        ret = 10*ret + d;
    }
    return ret;
}

ll solve(ll n)
{
    if(n <= 0) return 0;
    if(n == 1) return 1;
    ll e = 0, k = 1;
    while(k <= n) k *= 10, e++;
    e--, k /= 10;
    e = e/2+1, k = 1;
    while(e>0) k *= 10, e--;
    ll n1 = n/k;
    n1 *= k;
    ll need = n%k;
    if(need == 0) return solve(n-1) + 1;
    if(n1 == 0) return need;
    ll next = rev(n1+1);
    if(next == n1+1) need++, next -= 2;
    //cout << n << " " << k << " next is " << next << " with " << need << "\n";
    //getchar();
    return solve(next) + need;
}

int main()
{
    /*f(i,1,1000000) DP[i] = INF;
    DP[1] = 1;

    f(i,1,1000000)
    {
        DP[i+1] = min(DP[i+1], DP[i] + 1);
        int r = rev(i);
        DP[r] = min(DP[r], DP[i] + 1);
    }*/

    fin >> T;

    f(t,1,T)
    {
        fin >> N;
        fout << "Case #" << t << ": " << solve(N) << "\n";
    }
}
