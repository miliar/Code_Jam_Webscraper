// RandomUsername (Nikola Jovanovic)
// GCJ 2016 R2
// A

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000
#define MAXN

using namespace std;

int t;
int n;
int p, r, s;
string ret = "X";

string expand(string S)
{
    int sz = S.size();
    string ret = "";
    ff(i, 0, sz-1)
    {
        if(S[i] == 'R') ret += "RS";
        if(S[i] == 'P') ret += "PR";
        if(S[i] == 'S') ret += "SP";
    }
    return ret;
}

enum digs{RR, PP, SS};
int cnt[500];

string flip(string S)
{
    int sz = S.size();
    if(sz == 1) return S;
    string L = flip( S.substr(0, sz/2) );
    string R = flip( S.substr(sz/2, sz/2) );
    if(L < R) return L + R;
    else return R + L;
}

bool valid(string S)
{
    cnt['R'] = cnt['P'] = cnt['S'] = 0;
    int sz = S.size();
    ff(i, 0, sz-1)
    {
        cnt[ S[i] ]++;
    }
    if(cnt['R'] != r) return false;
    if(cnt['P'] != p) return false;
    if(cnt['S'] != s) return false;
    return true;
}

void solve(string S)
{
    ff(i, 1, n)
        S = expand(S);
    S = flip(S);
    if(valid(S) && (ret[0] == 'X' || S < ret))
        ret = S;
}

int main()
{
    //freopen("A.out", "w", stdout);
    scanf("%d", &t);
    ff(tt, 1, t)
    {
        ret[0] = 'X';
        scanf("%d %d %d %d", &n, &r, &p, &s);
        solve("R");
        solve("P");
        solve("S");
        cout << "Case #"<<tt<<": ";
        if(ret[0] == 'X') cout << "IMPOSSIBLE" << endl;
        else cout << ret << endl;
    }

    return 0;
}