#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define pii pair<int,int>
#define vii vector<pii>
#define rep(i,n) for(int i = 0; i < n; i++)
#define rp(i,a,n) for(int i=a;i<=int(n);i++)
#define IT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define all(x) (x).begin(), (x).end()
#define ll long long
#define sc(x) scanf("%d", &x)
#define oo 1000000000
#define fill(a,b) memset(a,b,sizeof a)
#define F first
#define S second
#define mod 1000000007
#define N 10005
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
using namespace std;
bool ok(string s)
{
    int ind=1;
    rep(i,s.size()) if(s[i]=='-') ind=0;
    return ind;
}
int main()
{
    freopen("lol.in","r",stdin);
    freopen("lol.out","w",stdout);
    int t;
    cin >> t;
    rp(tt,1,t)
    {
        string s;
        int ans=0,x=0;
        cin >> s;
        while(!ok(s))
        {
            rep(i,s.size()) if(s[i]=='-') x=i;
            int j=0;
            while(s[j]=='+'&&j<s.size()) j++;j--;
            if(j>=0) x=j;
            reverse(s.begin(),s.begin()+x+1);
            rp(i,0,x) if(s[i]=='+') s[i]='-';else s[i]='+';
            ans++;
        }
        printf("Case #%d: %d\n",tt,ans);
    }

}
