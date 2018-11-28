#include <bits/stdc++.h>
#include <windows.h>

#define f first
#define s second
#define ll long long
#define ld long double
#define pb push_back
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define pii pair<int,int>
#define vi vector<int>

using namespace std;

const int inf=2e9;
const double eps=1e-9;
const int maxn = 3e5 + 500, base = 1e9+7;

void solve()
{
    string s;
    cin >> s;
    int ans = 0;
    for (int i=1;i<s.size();i++){
        if (s[i] != s[i - 1])
            ans++;
    }
    if (s[s.size() - 1] == '-')
        ans++;
    printf("%d\n", ans);
}
int main()
{
    files1;
    files2;
    int t;
    fast_io;
    cin.tie(0);
    cin >> t;
    for (int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
