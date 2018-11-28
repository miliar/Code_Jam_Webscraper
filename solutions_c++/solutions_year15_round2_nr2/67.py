#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------

ifstream fin("B.TXT");
ofstream fout("B.OUT");

int Ans, H, W, N, T, Neg[10];

int neighs(int i, int j, int h, int w)
{
    int ret = 0;
    if(i-1 >= 1) ret++;
    if(j-1 >= 1) ret++;
    if(i+1 <= h) ret++;
    if(j+1 <= w) ret++;
    return ret;
}

int solve(int h, int w, int n, int type)
{
    int ret = 0;
    if(n == 0) return 0;
    if(w == 1) return n-1;
    f(i,1,h)
    {
        int st = i%2 ? 1 : 2;
        if(type) st = st == 2 ? 1 : 2;
        for(int j = st; j <= w; j += 2) n--;
    }
    Neg[0] = Neg[1] = Neg[2] = Neg[3] = Neg[4] = 0;
    f(i,1,h)
    {
        int st = i%2 ? 2 : 1;
        if(type) st = st == 2 ? 1 : 2;
        for(int j = st; j <= w; j += 2) Neg[neighs(i,j,h,w)]++;
    }
    int i = 0, neg = 0;
    while(n > 0)
    {
        while(neg < 5 && Neg[neg] == 0) neg++;
        ret += neg, Neg[neg]--;
        n--;
    }
    return ret;
}

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> H >> W >> N;
        cout << t << "\n";
        int s1 = solve(H,W,N,0);
        int s1a = solve(H,W,N,1);
        int s2 = solve(W,H,N,0);
        int s2a = solve(W,H,N,1);
        int ans = min(s1,s1a);
        ans = min(ans,s2);
        ans = min(ans,s2a);
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
