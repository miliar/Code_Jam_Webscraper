#include<bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define M 1000000009
#define REM 4
#define N 100005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define f(i,n) for(i=0;i<n;i++)
#define foi(i,j,k) for(i=j;i<k;i++)
#define mll map<ll,ll>
#define foe(i,j,k) for(i=j;i<=k;i++)
 
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;
 
int main()
{
    ll t,i,j,k,l;
    cin>>t;l=1;
 int arr[26]={0};
    while(t--)
    {
      string s;
      vector <int> v;
      for(i=0;i<26;i++)arr[i]=0;
 
      cin>>s;
      k=s.length();
      for(i=0;i<k;i++)
      {
        arr[s[i]-'A']++;
      }
 
      while(arr['Z'-'A']!=0){arr['E'-'A']--;arr['R'-'A']--;arr['O'-'A']--;arr['Z'-'A']--;v.pb(0);}
      while(arr['W'-'A']!=0){arr['T'-'A']--;arr['O'-'A']--;arr['W'-'A']--;v.pb(2);}
      while(arr['U'-'A']!=0){arr['F'-'A']--;arr['R'-'A']--;arr['O'-'A']--;arr['U'-'A']--;v.pb(4);}
      while(arr['X'-'A']!=0){arr['S'-'A']--;arr['I'-'A']--;arr['X'-'A']--;v.pb(6);}
      while(arr['G'-'A']!=0){arr['G'-'A']--;arr['I'-'A']--;arr['E'-'A']--;
      arr['H'-'A']--;arr['T'-'A']--;v.pb(8);}
      while(arr['O'-'A']!=0){arr['O'-'A']--;arr['N'-'A']--;arr['E'-'A']--;v.pb(1);}
      while(arr['H'-'A']!=0){arr['H'-'A']--;arr['T'-'A']--;arr['E'-'A']--;arr['E'-'A']--;
      arr['R'-'A']--;v.pb(3);}
 
while(arr['F'-'A']!=0){arr['F'-'A']--;arr['I'-'A']--;arr['E'-'A']--;arr['V'-'A']--;
      v.pb(5);}
      while(arr['S'-'A']!=0){arr['S'-'A']--;arr['E'-'A']--;arr['V'-'A']--;arr['E'-'A']--;
      arr['N'-'A']--;v.pb(7);}
      while(arr['E'-'A']!=0){arr['E'-'A']--;arr['N'-'A']--;arr['N'-'A']--;arr['I'-'A']--;
      v.pb(9);}
 
     sort(v.begin(),v.end());
 
     cout<<"Case #"<<l++<<": ";
     k=v.size();
     for(i=0;i<k;i++) cout<<v[i];
      cout<<endl;
 
 
    }
}