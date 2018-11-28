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

int T;

ifstream fin("A.in");
ofstream fout("A_out.txt");

bool Win[4][4];
char CH[4];
int A[4], N;
string Ans;
vector<int> V;

bool ok(vector<int> v)
{
    if(SZ(v) == 1) return true;
    for(int i = 0; i < SZ(v); i += 2) if(v[i] == v[i+1]) return false;
    vector<int> q;
    for(int i = 0; i < SZ(v); i += 2)
    {
        if(Win[v[i]][v[i+1]]) q.pb(v[i]);
        else q.pb(v[i+1]);
    }
    return ok(q);
}

void work(int rem, string curr)
{
    if(rem == 0)
    {
        if(ok(V)) Ans = min(Ans, curr);
        return;
    }

    f(i,1,3) if(A[i])
    {
        A[i]--;
        V.pb(i);
        work(rem-1, curr + CH[i]);
        V.pop_back();
        A[i]++;
    }
}

int main()
{
    fin >> T;

    CH[1] = 'R';
    CH[2] = 'P';
    CH[3] = 'S';

    f(tt,1,T)
    {
        cout << tt << "\n";
        Win[1][3] = Win[2][1] = Win[3][2] = true;
        fin >> N >> A[1] >> A[2] >> A[3];
        Ans = "Z";
        work(1<<N, "");
        if(Ans != "Z") fout << "Case #" << tt << ": " << Ans << "\n";
        else fout << "Case #" << tt << ": IMPOSSIBLE\n";
    }
}
