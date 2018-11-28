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

main()
{
    int t,sm;
    int tot[1001];
    char str[1010];
    r(t);
    int k = 1;
    while(t--)
    {
        r(sm);
        rs(str);
        tot[0] = str[0]-'0';
        int ans = 0;
        fr(i,1,sm)
        {
            int temp = 0;
            if(tot[i-1] < i && str[i] > '0' )
            {
                temp = (i-tot[i-1]);
            }
            tot[i] = tot[i-1] + (str[i]-'0') + temp;
            ans += temp;
        }
       P("Case #%d: %d\n",k,ans);
       k++;
    }
    return 0;
}
