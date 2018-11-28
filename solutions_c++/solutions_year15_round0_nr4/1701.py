#include<bits/stdc++.h>
using namespace std;

#define p(n) printf("%d\n",n)
#define r(n) scanf("%d",&n)
#define rs(n) scanf("%s",n)
#define ps(n) printf("%s\n",n)
#define P printf
#define R scanf
#define F first
#define S second
#define fr(i,a,b) for(int i=(int)a; i <= (int)b; i++)
#define frr(i,a,b) for(int i=(int)a; i >= (int)b; i--)
#define ll long long int
#define pb push_back
#define vi vector<int>
#define ve(x) vector<x>
#define si set<int>
#define itv vi :: iterator
#define ixv(x) vector<x> :: iterator
#define its si :: iterator
#define ixs(x) set<x> :: iterator
#define fill(s,v) memset(s,v,sizeof(s))
#define all(s) s.begin(),s.end()
#define fs(i,s) for(its i = s.begin(); i != s.end(); i++)
#define fv(i,v) for(itv i = v.begin(); i != v.end(); i++)
#define INF INT_MAX
#define MOD 1000000007
#define ii pair<int,int>
#define mp make_pair

ll ipow(ll base, ll exp)
{
    ll result = 1;
    while (exp)
    {
        if (exp & 1)
            {result *= base;result %= MOD;}
        exp >>= 1;
        base *= base;
        base %= MOD;
    }
    return result;
}
bool rich[5][5][5];
main()
{
    fill(rich[1],false);
    fill(rich[2],false);
    rich[2][1][1] = rich[2][1][3] = rich[2][3][3] = true;
    fill(rich[3],true);
    rich[3][2][3] = rich[3][3][3] =rich[3][3][4] = false;
    fill(rich[4],true);
    rich[4][4][4] = rich[4][3][4]=false;
    int t;
    r(t);
    int X,R,C;
    int k = 1;
    while(t--)
    {
        cin >> X >> R >>C;
        if(R > C) swap(R,C);
        P("Case #%d: ",k);
        k++;
        if(rich[X][R][C]) ps("RICHARD");
        else ps("GABRIEL");
    }
    return 0;
}
