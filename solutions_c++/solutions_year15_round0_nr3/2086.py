#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define sqr(x)      (x)*(x)
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
#define MOD         100007
#define eps         1e-9
#define MAX         1440

typedef long long int LL;
typedef double db;
int dp[10010][6][6];
int A[5][10];
map<char,int> m;
string s;
int s1[10010], curr;
bool call(int pos, int nw, int subs)
{
    //D(pos);
    //D(nw);
    //D(subs);
    //cout << endl;
    if(pos == curr)
    {
        if(nw == 4 && subs == 4)
            return 1;
        return 0;
    }
    if(dp[pos][nw][subs] != -1)
            return dp[pos][nw][subs];
    int nxt = nw;
    if(nw < 0)
        nxt = -nxt;
    nxt = A[nxt][s1[pos]];
    if(nw < 0)
        nxt = -nxt;
    bool ret = call(pos+1, nxt, subs);
    if(nxt == subs)
        ret = max(ret,call(pos+1, 1, subs+1));
    return dp[pos][nw][subs] = ret;
}

//int dx[] = {+0,+1,+0,-1};
//int dy[] = {+1,+0,-1,+0};
//int dx[] = {-1,-1,-1,+0,+0,+1,+1,+1};
//int dy[] = {-1,+0,+1,-1,+1,-1,+0,+1};
//bool check(int n, int pos) {return (bool) (n & (1<<pos));}
//int on(int n, int pos) {return n | (1<<pos); }
//int off(int n, int pos) {return n & ~(1<<pos); }

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //ios_base::sync_with_stdio(0); cin.tie(0);
    int i,j,k,cs,t,L,X;
    m['i'] = 2;
    m['j'] = 3;
    m['k'] = 4;

    A[1][1] = 1;
    A[1][2] = 2;
    A[1][3] = 3;
    A[1][4] = 4;

    A[2][1] = 2;
    A[2][2] = -1;
    A[2][3] = 4;
    A[2][4] = -3;

    A[3][1] = 3;
    A[3][2] = -4;
    A[3][3] = -1;
    A[3][4] = 2;

    A[4][1] = 4;
    A[4][2] = 3;
    A[4][3] = -2;
    A[4][4] = -1;


    sf(t);
    FRE(cs,1,t)
    {
        mem(dp,-1);
        sff(L,X);
        cin >> s;
        //D(s);
        curr = 0;
        for(i = 1; i<=X; i++)
        {
            for(j = 0; j<s.sz; j++)
                s1[curr++] = m[s[j]];
        }
        //FRL(i,0,curr)
          //  D(s1[i]);
        pf("Case #%d: ",cs);
        if(call (0,1,2))
            pf("YES\n");
        else
            pf("NO\n");
    }
    return 0;
}

