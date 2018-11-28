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


double Yes[66000], No[66000], P[20];
int K, N, T;

ifstream fin("B.in");
ofstream fout("B_out.txt");

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << tt << "\n";
        fin >> N >> K;
        f(i,0,N-1) fin >> P[i];
        f(m,0,(1<<N)-1)
        {
            No[m] = 1;
            Yes[m] = 1;
            f(i,0,N-1) if(m&(1<<i)) Yes[m] *= P[i], No[m] *= (1.0 - P[i]);
        }
        double ans = 0;
        f(m,0,(1<<N)-1)
        {
            if(__builtin_popcount(m) == K)
            {
                vector<int> v;
                f(i,0,N-1) if(m&(1<<i)) v.pb(i);
                double prob = 0;
                f(sub,0,(1<<K)-1) if(__builtin_popcount(sub) == K/2)
                {
                    int sub_mask = 0;
                    f(i,0,(K-1)) if(sub&(1<<i)) sub_mask += (1<<v[i]);
                    prob += Yes[m-sub_mask] * No[sub_mask];
                }
                ans = max(ans, prob);
            }
        }
        fout << "Case #" << tt << ": " << setprecision(12) << fixed << ans << "\n";
    }
}
