#include <bits/stdc++.h>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define FORR(i,j,k,l) for(int i=j;i<=k;i+=l)
#define inf         freopen("in.txt", "r", stdin)
#define outf        freopen("out.txt", "w", stdout)
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c)    scanf("%d %d %d", &a, &b, &c)
#define minn          (long long)-1000000000000000000
#define maxx          (long long) 1000000000000000000
#define mod          1000000007
#define LL           long long
#define NL '\n'
#define cnd tree[idx]
#define lnd (2*idx)
#define rnd ((2*idx)+1)
#define PB push_back
#define F first
#define S second
#define MK make_pair
typedef pair<int,int> pr;

string str;
int ar[100010], cnt[100010];
int main()
{
    ios::sync_with_stdio(false);
    inf;
    outf;
    int tc;
    cin>>tc;
    FOR(tt,1,tc)
    {
        LL i,j,x,y,n,m,a=0,b=0,c=0,k;
        cin>>str; n=str.size();
        cin>>k;
        FOR(i,0,n-1)
        {
            if(str[i]=='-'&&i+k-1>=n) a=1;
            else if(str[i]=='-')
            {
                c++;
                FOR(j,i,i+k-1)
                {
                   if(str[j]=='-') str[j]='+';
                   else str[j]='-';
                }
            }
        }
        if(a==1)cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<NL;
        else cout<<"Case #"<<tt<<": "<<c<<NL;
    }
    return 0;
}


