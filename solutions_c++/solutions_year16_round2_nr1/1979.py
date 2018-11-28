#include<bits/stdc++.h>
using namespace std;
 
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 10045
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

vector<ll>v;
ll c[30];
int main()
{
  ll tc,j,k,i;
  string str;
  cin>>tc;
  f(j,tc)
  {
    f(i,26)
    c[i]=0;
    v.clear();
  cin>>str;
  ll l=str.length();
  f(i,l)
  c[str[i]-'A']++;
  if(c['Z'-'A']>0)
  {
    k=c['Z'-'A'];
    f(i,k)
    v.pb(0);
    c['Z'-'A']-=k;
    c['E'-'A']-=k;
    c['R'-'A']-=k;
    c['O'-'A']-=k;


  }
  if(c['W'-'A']>0)
  {
    k=c['W'-'A'];
    f(i,k)
    v.pb(2);
    c['T'-'A']-=k;
    c['W'-'A']-=k;
    c['O'-'A']-=k;
     


  }
  if(c['U'-'A']>0)
  {
    k=c['U'-'A'];
    f(i,k)
    v.pb(4);
    c['F'-'A']-=k;
    c['O'-'A']-=k;
    c['U'-'A']-=k;
    c['R'-'A']-=k;
     
     


  }
  if(c['X'-'A']>0)
  {
    k=c['X'-'A'];
    f(i,k)
    v.pb(6);
    c['S'-'A']-=k;
    c['I'-'A']-=k;
    c['X'-'A']-=k;
    
     


  }
  if(c['G'-'A']>0)
  {
    k=c['G'-'A'];
    f(i,k)
    v.pb(8);
    c['E'-'A']-=k;
    c['I'-'A']-=k;
    c['G'-'A']-=k;
    c['H'-'A']-=k;
    c['T'-'A']-=k;
     


  }
  if(c['R'-'A']>0)
  {
    k=c['R'-'A'];
    f(i,k)
    v.pb(3);
    c['T'-'A']-=k;
    c['H'-'A']-=k;
    c['R'-'A']-=k;
    c['E'-'A']-=k;
    c['E'-'A']-=k;
     


  }
  if(c['F'-'A']>0)
  {
    k=c['F'-'A'];
    f(i,k)
    v.pb(5);
    c['F'-'A']-=k;
    c['I'-'A']-=k;
    c['V'-'A']-=k;
    c['E'-'A']-=k;
     
     


  }
  if(c['S'-'A']>0)
  {
    k=c['S'-'A'];
    f(i,k)
    v.pb(7);
    c['S'-'A']-=k;
    c['E'-'A']-=k;
    c['V'-'A']-=k;
    c['E'-'A']-=k;
    c['N'-'A']-=k;
     


  }
  k=c['O'-'A'];
  f(i,k)
  v.pb(1);
  k=c['I'-'A'];
  f(i,k)
  v.pb(9);

sort(v.begin(),v.end());
cout<<"Case #"<<j+1<<": ";
l=v.size();
f(i,l)
cout<<v[i];
cout<<endl;
}



}