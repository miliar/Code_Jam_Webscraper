#include<bits/stdc++.h>
#define f(i,a,b) for(int i=a;i<b;i++)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define EPS 1e-9
#define PI acos(-1)
#define INF 2000000000
#define mod 1000000007
#define trace(x)    cerr << #x << ": " << x << endl;
#define forit(it,m) for(typeof(m.begin()) it=m.begin();it!=m.end();++it)
#define MOD 1000 

#define pr16
 
#ifdef pr16
  #define pr(x)                 cerr << #x << ": " << x << endl;
  #define pr2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
  #define pr3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
  #define pr4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
  #define pr5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
  #define pr6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl;
  #define prc(a) tr(a, it) cerr<<*(it)<<" "; cerr<<endl
  #define pra(a,n) for(int i=0; i<(n); i++) cerr<<((a)[i])<<" "; cerr<<"\n"
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl; 
  #define prddd(a,x,y,z) for(int i=0;i<x;i++) {cerr<<"layer "<<i<<":\n";prdd(a[i],y,z)}
 
#else
  #define pr(x)
  #define pr2(x, y)
  #define pr3(x, y, z)
  #define pr4(a, b, c, d)
  #define pr5(a, b, c, d, e)
  #define pr6(a, b, c, d, e, f)
  #define tr(c,it)
  #define prc(a)
  #define pra(a,n)
  #define prdd(a, r, c)
  #define prddd(a,x,y,z)
#endif

using namespace std;
typedef long long ll  ;
typedef pair<int,int> ii  ;
typedef vector<int> vi ; 
typedef unsigned long long ull ; 
typedef pair<ll,ll> ill  ; 



int x[40010] ; 


inline int prod(int a , int b) 
{ 
	
	if(a<0) return -prod(-a,b) ; 
    if(b<0) return -prod(a,-b) ;  
    
    if(a==1) return b ; 
    if(b==1) return a ; 
    
    if(a==b) return -1 ;  
    
    if(a==2)
    {  
       if(b==3) return 4 ; 
       if(b==4) return -3 ; 
    }
    
    if(a==3) 
    { 
       if(b==2) return -4 ;  
       if(b==4) return 2 ; 
    }
    
    if(a==4) 
    {  if(b==2) return 3 ; 
       if(b==3) return -2; 
    }
}
    
       
int binpow(ll base,ll pot) 
{    
     
     if(pot==1) 
     { return base ; } 
     
     if(pot%2==0) 
     { int k= binpow(base, pot/2) ; 
       return prod(k,k) ; 
     }
     
     int k=binpow(base, pot-1)  ; 
     return prod(k,base) ; 
}
       
     
     
     
       
map<char,int>mapa; 

int main()
{ 
    ios::sync_with_stdio(0);
    freopen ("C-large.in", "r", stdin);
	freopen ("C-large.out", "w", stdout);	
    
    ll  t ;  
    cin>>t  ; 
    mapa['i']=2 ; 
    mapa['j']=3 ; 
    mapa['k']=4; 
    f(o,0,t)  
    {  
      ll l , pot;  
      cin>>l>>pot  ; 
      
      f(i,0,4*l+5) x[i]=0 ;  
      
      string s ; cin>>s ; 
      x[0]= mapa[s[0]] ; 
      
      for(ll i=1;i<min(4*l+5,pot*l);i++) 
      x[i]= prod(x[i-1], mapa[s[i%l]]) ;  
      
      bool ok=0 ; 
      
      bool ok1=0 ; 
      ll fi=INF; 
      ll fk=INF  ; 
      for(ll i=0;i<min(4*l+5,pot*l);i++) 
      if(x[i]==2) { fi=i;break; } 
      
      for(ll i=fi;i<min(4*l+5,pot*l);i++) 
      if(x[i]==4) { fk=i; break; } 
      
      if(fi!=INF && fk!=INF && fi<fk) ok1=1;  
      
      int r= binpow(x[l-1], pot) ;  
      
      if(r==-1) ok=1 ; 
      
      if(ok&&ok1) 
      cout<<"Case #"<<o+1<<": YES"<<endl ; 
      else 
      cout<<"Case #"<<o+1<<": NO"<<endl ; 
    }
    
    
    return 0  ; 
}
      
      
      
      
      
      
