#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
const int maxn = 4;
string ans;
char a[1 << maxn];
int p, r, s, n, cnt, x;
char battle(char c1, char c2)
{
    if(c2 < c1)swap(c1, c2);
    if(c1 == 'R' && c2 == 'S')return 'R';
    if(c1 == 'P' && c2 == 'R')return 'P';
    if(c1 == 'P' && c2 == 'S')return 'S';
}
void _main()
{
    ans = ""; cnt = 0; int tmp = 0;
    cin >> n >> r >> p >> s;
    x = 1 << n;
    for(int i = cnt; i < cnt+p; i++)a[i] = 'P';
    cnt += p;
    for(int i = cnt; i < cnt+r; i++)a[i] = 'R';
    cnt += r;
    for(int i = cnt; i < cnt+s; i++)a[i] = 'S';
    do
    {
        string c = "", d = "";
        bool ok = 1;
        for(int i = 0; i < 1<<n; i++)c += a[i];
        for(int k = 0; k < n; k++)
        {
            for(int i = 0; i < c.size(); i+=2)
            {
                if(c[i] == c[i+1])
                {
                    ok = 0;
                    break;
                }
                d += battle(c[i], c[i+1]);
                if(!ok)break;
            }
            swap(c, d); d = "";
            if(!ok)break;
        }
        if(ok)
        {
            c = "";
            for(int i = 0; i < 1<<n; i++)c += a[i];
            if(c < ans || ans == "")ans = c;
        }
        tmp++;
    }while(next_permutation(a, a + x));
    //cout << tmp << "\n";
}
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt0(6).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt; cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        _main();
        if(ans == "")ans = "IMPOSSIBLE";
        cout << "Case #" << i << ": " << ans << "\n";
    }
    return 0;
}
