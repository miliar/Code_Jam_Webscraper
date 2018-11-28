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

bool U[15];
int T;
ll N;

ifstream fin("A.in");
ofstream fout("A_out.out");

void mark(ll n)
{
    while(n)
    {
        U[n%10] = true;
        n /= 10;
    }
}

bool ok()
{
    f(i,0,9) if(!U[i]) return false;
    return true;
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> N;
        if(N == 0)
        {
            fout << "Case #" << tt << ": INSOMNIA\n";
            continue;
        }
        f(i,0,9) U[i] = false;
        for(ll i = N; i >= 0; i += N)
        {
            mark(i);
            if(ok())
            {
                fout << "Case #" << tt << ": " << i << "\n";
                break;
            }
        }
    }
}
