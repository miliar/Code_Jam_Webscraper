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

ifstream fin("B.txt");
ofstream fout("B.out");

int A[1005], N, T;

int solve(int k)
{
    int ret = k;
    f(i,1,N) ret += (A[i]-1) / k;
    return ret;
}

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> N;
        f(i,1,N) fin >> A[i];
        int ans = INF;
        f(i,1,1000) ans = min(ans,solve(i));
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
