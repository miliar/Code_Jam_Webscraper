
#include<bits/stdc++.h>
//#include <windows.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define sqr(x)      ((x)*(x))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define D(x)        cout<<#x " = "<<(x)<<endl
#define pf          printf
#define VI          vector <int>
#define pii         pair <int, int>
#define pll         pair <LL, LL>
#define pb          push_back
#define mp          make_pair
#define pi          acos(-1.00)
#define DBG         pf("Hi\n")
#define sz          size()
#define ins         insert
#define fi          first
#define se          second
#define xx          first
#define yy          second
#define inf         (1<<29)
#define hp          (LL) 999983
#define MOD         100007
#define eps         1e-9
#define MAX         10000

typedef long long int LL;
typedef double db;

//int dx[] = {+0,+1,+0,-1};
//int dy[] = {+1,+0,-1,+0};
//int dx[] = {-1,-1,-1,+0,+0,+1,+1,+1};
//int dy[] = {-1,+0,+1,-1,+1,-1,+0,+1};
//bool check(LL n, int pos) {return (bool) (n & ((LL)1<<pos));}
//LL on(LL n, int pos) {return n | ((LL)1<<pos); }
//LL off(LL n, int pos) {return n & ~((LL)1<<pos); }


char key[] = "ijk";
int arr[150][150];
int dp[MAX+10][5][5][5];

int sign(char a, char b)
{
    if(a == '1' || b == '1') return 1;
    if(a == b) return -1;
    return arr[a][b];
}

char next_char(char a, char b)
{
    if(a == '1') return b;
    if(b == '1') return a;
    if(a == b) return '1';
    for(int i = 0; i < 3; i++)
        if(key[i] != a && key[i] != b)
            return key[i];
}

string str, in;

int f(char pre)
{
    if(pre == '1') return 1;
    if(pre == 'i') return 2;
    if(pre == 'j') return 3;
    if(pre == 'k') return 4;
}

int g(int sgn)
{
    if(sgn == -1) return 0;
    return 1;
}

bool calc(int idx, char pre, int sgn, int lk)
{
    if(idx == str.sz) return (sgn == 1 && lk == 3 && pre == '1');

    if(dp[idx][f(pre)][g(sgn)][lk] != -1) return dp[idx][f(pre)][g(sgn)][lk];

    if(lk > 2) return 0;

    char nc;
    int ns;

    ns = sign(pre, str[idx]);
    nc = next_char(pre, str[idx]);
    if(nc != key[lk]) return dp[idx][f(pre)][g(sgn)][lk] = calc(idx+1, nc, sgn*ns, lk);
    return dp[idx][f(pre)][g(sgn)][lk] = calc(idx+1, '1', sgn*ns, lk+1)  || calc(idx+1, nc, sgn*ns, lk);
}

int main()
{
    freopen("c:\\Users\\User\\Desktop\\in.txt", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);
    //ios_base::sync_with_stdio(0); cin.tie(0);
    arr['i']['j'] = 1;
    arr['j']['i'] = -1;
    arr['i']['k'] = -1;
    arr['k']['i'] = 1;
    arr['j']['k'] = 1;
    arr['k']['j'] = -1;

    int i, j, k, t, cs, n, m, mn, mx, len, x;

    sf(t);
    FRE(cs,1,t)
    {
        mem(dp, -1);

        sff(len, x);
        cin >> in;
        str = "";

        while(x--)
            str = str + in;
        pf("Case #%d: %s\n", cs, calc(0,'1',1, 0)? "YES":"NO");
    }

    return 0;
}



