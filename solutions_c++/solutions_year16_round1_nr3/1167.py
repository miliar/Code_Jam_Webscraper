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

int N, T, B[15];

int check(vector<int> &p, int sz)
{
    /*cout << "Checking ";
    for(int x : p) cout << x << " ";
    cout << " for size " << sz << "\n";*/
    f(i,0,sz-1)
    {
        int l = i == 0 ? sz-1 : i-1;
        int r = i == sz-1 ? 0 : i+1;
        int kid = p[i];
        int kid_l = p[l];
        int kid_r = p[r];
        //cout << "I'm at " << kid << " and neighs are " << kid_l << " and " << kid_r << "\n";
        //getchar();
        if(B[kid] != kid_l && B[kid] != kid_r) return false;
    }
    //cout << "It's good\n";
    return true;
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << "Case << " << tt << "\n";
        fin >> N;
        f(i,1,N) fin >> B[i];
        vector<int> perm;
        f(i,1,N) perm.pb(i);
        int ans = 2;
        do
        {
            f(sz,2,N) if(check(perm,sz)) ans = max(ans, sz);
        }while(next_permutation(all(perm)));
        fout << "Case #" << tt << ": " << ans << "\n";
    }
}
