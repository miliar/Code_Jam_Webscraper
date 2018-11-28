#include<bits/stdc++.h>
using namespace std;
 
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 100045
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

list<char>v;
list<char>::iterator it;
int main()
{
  /*
  freopen("input.io","r",stdin);
  freopen("output.txt","w",stdout);
  */
  ll t,i,j;
  string str;
  cin>>t;
  f(j,t)
  {
    cin>>str;
    ll len=str.length();
    ll stt,cur;
    v.pb(str[0]);
    stt=0;
    FOR(i,1,len)
    {
    cur=i;
      //dbg(str[cur]);dbg(str[stt]);
      
      if(str[cur]>=str[stt])
       { 
        v.pf(str[cur]);
        stt=cur;
      }
      else
        v.pb(str[cur]);
    }
    cout<<"Case #"<<j+1<<": ";
    for(it=v.begin();it!=v.end();it++)
    cout<<*it;
    cout<<endl;
    v.clear();
  }
}