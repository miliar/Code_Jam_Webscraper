#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define ff first
#define ss second

#ifndef ONLINE_JUDGE
#define dbg(args...)            {debug,args; cerr<<endl;}
#else
#define dbg(args...)
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
	{
	    cerr<<v<<" ";
	    return *this;
	}
} debug;

int res;
int n;
string grid[30];
int adj[30][30];
int mat[30][30];
vi ord;
int taken[30];

bool dfs(int id){
    if (id == n) return true;
    int i = ord[id];
    bool poss = true;
    bool one = false;
    for (int j = 0; j < n; j++){
        if (mat[i][j] && taken[j] == 0){
            taken[j] = 1;
            one = true;
            poss &= dfs(id + 1);
            taken[j] = 0;
        }
    }
    return (poss && one);
}

void gen(int id){
    if (id == n * n){
        ord.resize(n);
        iota(ord.begin(), ord.end(), 0);
        do {
            memset(taken, 0, sizeof taken);
            if (dfs(0) == false) return;
        } while (next_permutation(ord.begin(), ord.end()));
        int diff = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                diff += mat[i][j] - adj[i][j];
        res = min(res, diff);
        return;
    }
    int i = id / n, j = id % n;
    if (adj[i][j] == 1){
        mat[i][j] = 1;
        gen(id + 1);
    } else {
        mat[i][j] = 0;
        gen(id + 1);
        mat[i][j] = 1;
        gen(id + 1);
    }
}

void solve(){
    cin >> n;
    for (int i = 0; i < n; i++) cin >> grid[i];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            adj[i][j] = (int) grid[i][j] - '0';

    res = INT_MAX;
    gen(0);
    cout << res << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
