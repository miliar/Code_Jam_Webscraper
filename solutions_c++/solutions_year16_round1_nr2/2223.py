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

ifstream fin("B.in");
ofstream fout("B_out.out");

bool UsedCol[25], U[25];
int A[25][25], L[25][25], N, T;
vector<int> Ans;

bool equal(int i, vector<int> &v)
{
    f(j,1,N) if(v[j-1] != L[i][j]) return false;
    return true;
}

void work(int take)
{
    if(SZ(Ans)) return;
    if(take == N+1)
    {
        f(j,1,N) UsedCol[j] = false;
        vector<int> unmark;

        f(j,1,N)
        {
            vector<int> v1;
            f(i,1,N) v1.pb(A[i][j]);
            f(l,1,2*N-1) if(!U[l] && equal(l,v1))
            {
                U[l] = true;
                UsedCol[j] = true;
                unmark.pb(l);
                break;
            }
        }

        int used = N + SZ(unmark);
        if(used == 2*N-1)
        {
            f(j,1,N) if(!UsedCol[j])
            {
                f(row,1,N) Ans.pb(A[row][j]);
                return;
            }
        }

        for(int q : unmark) U[q] = false;
        return;
    }
    f(idx,1,2*N-1) if(!U[idx])
    {
        bool good = true;

        f(j,1,N)
        {
            A[take][j] = L[idx][j];
            if(A[take][j] <= A[take-1][j]) good = false;
        }

        if(good)
        {
            U[idx] = true;
            work(take+1);
            U[idx] = false;
        }
    }
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << "Case " << tt << "\n";
        fin >> N;
        Ans.clear();
        f(i,1,2*N-1) f(j,1,N) fin >> L[i][j];
        f(i,1,2*N) U[i] = false;
        work(1);
        fout << "Case #" << tt << ":";
        for(int v : Ans) fout << " " << v;
        fout << "\n";
    }
}
