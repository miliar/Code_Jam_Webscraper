#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>

typedef long long ll;
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;

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
const ll INFLL = 1000000000000000002ll;
const ll MOD = 1000000007;

inline ll min(ll a, ll b, ll c){return min(min(a,b),c);}
inline ll min(ll a, ll b, ll c, ll d){return min(min(min(a,b),c),d);}
inline ll max(ll a, ll b, ll c){return max(max(a,b),c);}
inline ll max(ll a, ll b, ll c, ll d){return max(max(max(a,b),c),d);}

// --------------------------------------------------------------------------------------------

ifstream fin("A.in");
ofstream fout("A_out.out");

int S[1005];
int N, K, T;
string Str;

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> Str >> K;
        N = SZ(Str);
        f(i,1,N) S[i] = Str[i-1] == '+' ? 1 : 0;
        int cnt = 0;
        f(i,1,N-K+1) if(!S[i])
        {
            f(j,i,i+K-1) S[j] ^= 1;
            cnt++;
        }
        f(i,1,N) if(!S[i]) cnt = -1;
        if(cnt >= 0) fout << "Case #" << tt << ": " << cnt << "\n";
        else fout << "Case #" << tt << ": " << "IMPOSSIBLE\n";
    }
}
