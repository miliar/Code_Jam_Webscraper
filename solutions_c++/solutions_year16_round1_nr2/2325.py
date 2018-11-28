#include<bits/stdc++.h>
using namespace std;
 
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 25500
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

vector<ll>num;

ll x[maxs];


int main()
{
  /*
  freopen("input.io","r",stdin);
  freopen("output.txt","w",stdout);
  */
  ll t,i,j,maxi,k,n,p;
   
  cin>>t;
  f(j,t)
  { 
     
    cin>>n;
    maxi=-1;
    f(i,2*n-1)
    {
    f(p,n)
     { cin>>k;
      x[k]++;
      if(k>maxi)
        maxi=k;
        }
    }
     
    f(i,maxi+1)
    {
      if(x[i]%2==1)
        num.pb(i);
        x[i]=0;
    }

    sort(num.begin(),num.end());
    cout<<"Case #"<<j+1<<": ";
    ll siz=num.size();
    f(i,siz)
    cout<<num[i]<<" ";
    cout<<endl;
    num.clear();
    

     
  }
}