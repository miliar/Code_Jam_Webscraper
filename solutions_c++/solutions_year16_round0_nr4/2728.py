#include <bits/stdc++.h>
 using namespace std;
#define pb push_back
#define m_p make_pair
#define F first
#define S second
#define For(i,a,b) for(int i=a;i<b;i++)
#define Fore(i,a,b) for(int i=a;i<=b;i++)
#define rFor(i,a,b) for(int i=a;i>b;i--)
#define rFore(i,a,b) for(int i=a;i>=b;i--)
#define tr(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define all(a) a.begin(),a.end()
#define mem(a,b) memset(a,b,sizeof(a))
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<int,pii> pi3;
typedef pair<pii,pii> pi4;
typedef vector<int> vi;
typedef vector<pii> vpii;
void sc(int& a){scanf("%d",&a);}
void sc(lli& a){scanf("%lld",&a);}
void sc(int& a,int& b){sc(a);sc(b);}
void sc(lli& a,lli& b){sc(a);sc(b);}
void sc(int& a,int& b,int& c){sc(a,b);sc(c);}
void sc(lli& a,lli& b,lli& c){sc(a,b);sc(c);}
void prl(int a){printf("%d\n",a);}
void prl(lli a){printf("%lld\n",a);}
void prl(){printf("\n");}
void prs(int a){printf("%d ",a);}
void prs(lli a){printf("%lld ",a);}
void prl(lli a, lli b){cout<<a<<" "<<b<<" "<<endl;}
void prl(lli a, lli b, lli c){cout<<a<<" "<<b<<" "<<c<<" "<<endl;}
void prl(lli a, lli b, lli c, lli d){cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e, lli f){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<endl;}
int mod =1000000007;
lli modpow(lli a, lli b, lli mod){lli res=1;while(b>0){if(b&1)res=(res*a)%mod;a=(a*a)%mod;b=b/2;}return res%mod;}
lli pow(lli a, lli b){lli res=1;while(b>0){if(b&1)res=(res*a);a=(a*a);b=b/2;}return res;}
#define inf INT_MAX
#define linf LLONG_MAX
const int MAX = 1000005;
int a[10],b[10];
map<int,int>  mymap;
int main() {
  int t;
  sc(t);
 lli n,s,c,k,p,l;
 k=0;
  while(t--){
    k++;
    sc(n,c);
    sc(s);
    printf("Case #%lld: ",k);


    Fore(i,1,s)
    {

      prs(i);
    }
   
  prl();
  }
}  

