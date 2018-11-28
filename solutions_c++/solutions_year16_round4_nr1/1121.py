# include <bits/stdc++.h>
using namespace std;
# define fi cin
# define fo cout
# define x first
# define y second
# define ll long long
# define db long double
# define scn(x) scanf("%I64d",&x)
# define scan(x) scanf("%d",&x)
# define print(x) printf("%d ",x)
# define prnt(x) printf("%I64d ",x);
# define eol printf("\n")
# define IOS ios_base :: sync_with_stdio(0)
# define pe "Possible"
# define ie "Impossible"
# define halt(...) {fo << (__VA_ARGS__) << '\n';exit(0);}
# define rep(n) for (int qwerty = 1;qwerty <= n;++qwerty)
# define pp(n) cerr << #n << " = " << n << '\n'
# define ppp(v) for (auto it : v) cerr << it << ' ';cerr << '\n'
const int mod = 1e9 + 7;
string ans;
char Ans(char a,char b)
{
    if (a == b) return 0;
    if (a == 'R' && b == 'S') return 'R';
    if (a == 'S' && b == 'P') return 'S';
    if (a == 'P' && b == 'R') return 'P';
    return Ans(b,a);
}
string get(int r,int p,int s)
{
    if ((r + p + s) == 1)
    {
        if (r) return "R";
        if (p) return "P";
        if (s) return "S";
    }
    else
    {
        if ((p&1) && (s&1)) return get(r / 2,(p + 1) / 2,s / 2) + get(r / 2,p / 2,(s + 1) / 2);
        if ((p&1) && (r&1)) return get(r / 2,(p + 1) / 2,s / 2) + get((r + 1) / 2,p / 2,s / 2);
        return get((r + 1) / 2,p / 2,s / 2) + get(r / 2,p / 2,(s + 1) / 2);
    }
}
int main(void)
{
    int t;
    ifstream fi("input");
    ofstream fo("output");
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        ans = "";
        fo << "Case #" << cs << ": ";
        int n,r,p,s;
        fi>>n>>r>>p>>s;
        if (!(abs(r - p) <= 1 && abs(p - s) <= 1 && abs(s - r) <= 1)) fo << "IMPOSSIBLE\n";
        else fo << get(r,p,s) << '\n';
    }
    return 0;
}



