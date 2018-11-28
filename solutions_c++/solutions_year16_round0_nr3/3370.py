#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

typedef long long ll;
using namespace std;
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

const int INF = 1000000002;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

ifstream fin("C.in");
ofstream fout("C_out.out");

int N, T, J;
vector<int> Vec;

ll convert(int n, int base)
{
    ll ret = 0;
    fd(i,N-1,0) ret = ret*base + (n&(1<<i)?1:0);
    return ret;
}

ll check(ll x)
{
    for(ll i = 2; i*i <= x; i++) if(x%i == 0) return i;
    return 0;
}

string binary(int n)
{
    string ret = "";
    f(i,0,N-1) if(n&(1<<i)) ret += '1'; else ret += '0';
    reverse(all(ret));
    return ret;
}

bool isJam(int m)
{
    Vec.clear();
    f(base,2,10)
    {
        ll x = convert(m,base);
        ll val = check(x);
        if(val == 0) return false;
        else Vec.pb(val);
    }
    return true;
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> N >> J;

        vector<string> nums;
        vector<vector<int>> ans;

        for(int i = (1<<(N-1)) + 1; i < (1<<N); i += 2)
        {
            if(SZ(ans) == J) break;
            if(isJam(i)) ans.pb(Vec), nums.pb(binary(i));
        }

        fout << "Case #" << tt << ":\n";
        f(i,0,J-1)
        {
            fout << nums[i] << " ";
            for(int x : ans[i]) fout << x << " ";
            fout << "\n";
        }
    }
}
