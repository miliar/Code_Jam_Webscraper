#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <cmath>
#include <cstring>
#include <bitset>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define mp make_pair
#define pb push_back
#define bpc(a) __builtin_popcount(a)
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define forn(i,n) for(int i=0;i<(n);++i)
#define X first
#define Y second
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }

const int mod = 1e9 + 7;
const int inf = 1e9;

ll powm(ll a,ll p,ll m){ll r=1 % m;while(p){if(p&1)r=r*a%m;p>>=1;a=a*a%m;}return r;}

void solve(int c)
{
    int s, cnt = 0, ans = 0;
    char p[1010];
    scanf("%d%s", &s, p);
    for(int i = 0; i <= s; ++i)
        if(i <= cnt)
            cnt += p[i] - '0';
        else
        {
            ans += i - cnt;
            cnt = i + p[i] - '0';
        }
    printf("Case #%d: %d\n", c, ans);
}

int main()
{
    int t;
    scanf("%d", &t);
    forn(i, t)
        solve(i + 1);
    return 0;
}
