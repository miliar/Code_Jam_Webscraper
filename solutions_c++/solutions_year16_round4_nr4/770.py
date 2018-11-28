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

bool U[5];
int A[5][5], B[5][5], N;
int T;

ifstream fin("D.in");
ofstream fout("D_out.txt");

bool isok(vector<int> p, int curr)
{
    if(curr == SZ(p)) return true;
    bool ret = true, found = false;
    int w = p[curr];
    f(i,0,N-1) if(B[w][i] && !U[i])
    {
        found = true;
        U[i] = true;
        if(!isok(p, curr+1)) ret = false;
        U[i] = false;
    }
    return ret&found;
}

bool ok()
{
    vector<int> p;
    f(i,0,N-1) p.pb(i);
    do
    {
        if(!isok(p,0)) return false;
    }while(next_permutation(all(p)));
    return true;
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << tt << "\n";
        fin >> N;
        f(i,0,N-1)
        {
            string s;
            fin >> s;
            f(j,0,N-1) A[i][j] = s[j] - '0';
        }
        int ans = INF;
        int x = N*N;
        f(m,0,(1<<x)-1)
        {
            bool bad = false;
            int cost = 0;

            f(i,0,x-1)
            {
                int w = i/N;
                int mach = i%N;
                if(A[w][mach] && !(m&(1<<i))) bad = true;
                if(!A[w][mach] && (m&(1<<i))) cost++;
                if(m&(1<<i)) B[w][mach] = 1;
                else B[w][mach] = 0;
            }

            if(bad) continue;
            if(ok()) ans = min(ans, cost);
        }
        fout << "Case #" << tt << ": " << ans << "\n";
    }
}
