/* Pranet Verma */
/* Yeh mera template hai. Apna khud banao =_= */
#include <bits/stdc++.h>
using namespace std;
#define infinity (1000000007)
#define ll long long
#define ull unsigned long long
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define pip pair<int,pii>
#define pb push_back
#define mp make_pair
#define s(n) scanf("%d",&n)
#define s2(n,m) scanf("%d%d",&n,&m)
#define s3(n,m,l) scanf("%d%d%d",&n,&m,&l)
#define rep(i,n) for(int i=0;i<n;++i)
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
const int mod=1000000007;
int cnt[2344];
int res[4][4]=
{
  {0,1,2,3},
  {1,0,3,2},
  {2,3,0,1},
  {3,2,1,0}
};
int syn[4][4]=
{
  {1,1,1,1},
  {1,-1,1,-1},
  {1,-1,-1,1},
  {1,1,-1,-1}
};

struct K
{
  int ch;
  int sign;
  K(){}
  K(int ch,int sign)
  {
    this->ch=ch;
    this->sign=sign;
  }
  K operator * (const int o)const
  {
    // cout<<o<<endl;
    int ret=res[ch][o];
    int sn=sign*syn[ch][o];
    return K(ret,sn);
  }

};
int main()
{
  std::ios::sync_with_stdio(false);


    
  int t;
  cin>>t;
  for(int tt=1;tt<=t;++tt)
  {
    cout<<"Case #"<<tt<<": ";
    int l,x;
    cin>>l>>x;
    string temp;
    cin>>temp;
    string s;
    while(x--)
      s+=temp;
    K curr(0,1);

    int i=0;
    int ctr=0;
    for(i=0;i<s.size();++i)
    {
      int ch=s[i]-'i'+1;
      curr=curr*ch;
      
      // cout<<curr.ch<<" "<<curr.sign<<"\n";
      if(curr.ch==1 && curr.sign==1)
      {
        ++i;
        ++ctr;
        curr=K(0,1);
        break;
      }      
      
    }

    for(;i<s.size();++i)
    {
      char ch=s[i]-'i'+1;
      curr=curr*ch;
      // cout<<curr.ch<<" "<<curr.sign<<"\n";
      
      if(curr.ch==2 && curr.sign==1)
      {
        ++i;
        ++ctr;
        curr=K(0,1);
        break;
      }      
      
    }

    for(;i<s.size();++i)
    {
      char ch=s[i]-'i'+1;
      curr=curr*ch;
    }    

    if(ctr==2 && curr.ch==3 && curr.sign==1)
    {
      cout<<"YES\n";
    }
    else
      cout<<"NO\n";

  }
  
   


}