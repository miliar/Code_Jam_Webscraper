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
#define oo INT_MAX
#define sc(x) scanf("%d", &x)
#define fill(a,b) memset(a,b,sizeof a)
#define F first
#define S second
#define mod 1000000007
using namespace std;
bool ok(vector<pair<int,int> > v)
{
    sort(all(v));
    int s1=0,s2=0;
    rep(i,v.size()-1) s1+=v[i].F;s2=v[v.size()-1].F;
    return s1<=s2;
}
bool vide(vector<pair<int,int> > v)
{
    rep(i,v.size()) if(v[i].F!=0) return 0;
    return 1;
}
int main()
{
   freopen("lol.in","r",stdin);
   freopen("lol.out","w",stdout);
   int t;
   cin >> t;
   rp(tt,1,t)
   {
       cout << "Case #" << tt << ": " ;
       int n,x;
       vector<pair<int,int> > v;
       cin >> n;
       rep(i,n) { sc(x);v.pb(mp(x,i)); }
       while(1)
       {
           if(vide(v)) break;
           sort(all(v));
           cout << (char)(v[ v.size() - 1 ].S+'A');
           v[ v.size() - 1 ].F--;
           if(vide(v)) break;
           sort(all(v));
           int s1=0,s2=0;
           rep(i,v.size()-1) s1+=v[i].F;s2=v[v.size()-1].F;
           if(s2>s1) { cout << (char)(v[ v.size() - 1 ].S+'A');v[ v.size() - 1 ].F--;  }
           cout << " ";
       }
       cout << endl ;
   }
}
