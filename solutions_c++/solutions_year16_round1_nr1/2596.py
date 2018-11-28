#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long int
#define pb push_back
#define mp make_pair
#define lf long double
#define VI vector<ll>
#define ppl pair<ll,ll>
#define ppi pair<int,int>
#define  F first
#define S Second
#define ML map<ll,ll>
#define itm map<ll,ll>::iterator
#define f_inp ios_base::sync_with_stdio(false)
int main()
{
    f_inp;
    ll n,m,a,b,c,d;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
  ll t,j=1,i;
  ll ans=0;
  cin>>t;
  string str,temp,t3,t2;
  while(t>0)
  {
      t--;
      cin>>str;
      t2="";
      for(i=0;i<str.length();i++)
      {
          temp="";
          temp+=str[i];
          temp=temp+t2;
          t3=t2;
          t3+=str[i];
          if(t3>temp)
            t2=t3;
          else
            t2=temp;
      }
      cout<<"Case #"<<j<<": "<<t2<<endl;
      j++;
  }
    return 0;

}
