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

int T, N, D[4050];
string S;

string print(int m)
{
    string s;
    f(i,0,N-1) if(m&(1<<i)) s += '+'; else s += '-';
    return s;
}

int flip(int m, int r)
{
    int a = 0, b = r, ret = m;
    while(a <= b)
    {
        int ea = (1<<a);
        int eb = (1<<b);
        int sa = m&ea;
        int sb = m&eb;
        if(a == b)
        {
            if(sa) ret -= sa;
            else ret += ea;
            a++, b--;
            continue;
        }
        ret -= sa;
        ret -= sb;
        if(!sa) ret += eb;
        if(!sb) ret += ea;
        a++, b--;
    }
    return ret;
}

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> S;
        N = SZ(S);
        f(i,0,(1<<N)-1) D[i] = INF;
        queue<int> q;
        int init = 0;
        f(i,0,N-1) if(S[i] == '+') init += (1<<i);
        q.push(init);
        D[init] = 0;

        while(!q.empty())
        {
            int m = q.front();
            q.pop();

            f(i,0,N-1)
            {
                int nm = flip(m,i);
                if(D[nm] > D[m] + 1)
                {
                    D[nm] = D[m] + 1;
                    q.push(nm);
                }
            }
        }

        fout << "Case #" << tt << ": " << D[(1<<N)-1] << "\n";
    }
}
