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
ofstream fout("C_out.txt");

int DP[250000], N, T;
string A[20], B[20];

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << tt << "\n";
        fin >> N;
        f(i,0,N-1) fin >> A[i] >> B[i];
        f(i,0,(1<<N)-1) DP[i] = 0;
        f(m,0,(1<<N)-1)
        {
            f(next,0,N-1) if(!(m&(1<<next)))
            {
                bool first = false, second = false;
                f(i,0,N-1) if(m&(1<<i)) if(A[i] == A[next]) first = true;
                f(i,0,N-1) if(m&(1<<i)) if(B[i] == B[next]) second = true;
                if(first && second) DP[m + (1<<next)] = max(DP[m + (1<<next)], DP[m] + 1);
                else DP[m + (1<<next)] = max(DP[m + (1<<next)], DP[m]);
            }
        }
        fout << "Case #" << tt << ": " << DP[(1<<N)-1] << "\n";
    }
}
