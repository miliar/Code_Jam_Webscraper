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

ifstream fin("D.in");
ofstream fout("D_out.out");

int T;
ll K, C, S;

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> K >> C >> S;

        fout << "Case #" << tt << ":";
        ll add = 1;
        f(i,1,C-1) add *= K;
        ll l = 1;
        while(K)
        {
            fout << " " << l;
            l += add;
            K--;
        }
        fout << "\n";
    }
}
