
//Author : Ujjawal Dixit  , ABV-IIITM
//Task : test

#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX 1e9
#define MIN -1e9
using namespace std;
typedef double ld;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define FOR(i,n,m) for(int i=0;i<n;i+=m)
#define For(i,n,m) for(int i=1;i<=n;i+=m)
#define max(a,b)    (a>=b?a:b)
//#define min(a,b)    (a<b?a:b)
#define countbits(num)   __builtin_popcount(num)
#define countbitsll(num)   __builtin_popcountll(num)
#define s(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define p(a) printf("%d",a)
#define f(i,a,b) for(int i=a;i<b;i++)
#define pll(a) printf("%lld",a)
#define pln()  printf("\n")
#define getstr(in) getline(cin,in)
#define getc() getchar()
#define uj() int t; scanf("%d",&t); while(t--)
template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}
int main()
{ 
    
    int t ;  
  
  cin>>t ;  
  
  
  int x,r,c  ;  
  
  
  f(o,0,t) 
  {  
    cin>>x>>r>>c  ; 
    
    if(x==1) 
    { cout<<"Case #"<<o+1<<": "<<"GABRIEL"<<endl  ; 
      continue;  
    } 
    
    if(x==2) 
    { if((r*c)%2==0) { cout<<"Case #"<<o+1<<": "<<"GABRIEL"<<endl  ; continue; }
      else {cout<<"Case #"<<o+1<<": "<<"RICHARD"<<endl  ; continue;} 
    }
    
    if(x==3) 
    { if( (r*c)%3==0  && c>=2 && r>=2 ) 
      cout<<"Case #"<<o+1<<": "<<"GABRIEL"<<endl  ; 
      else 
      cout<<"Case #"<<o+1<<": "<<"RICHARD"<<endl  ; 
      continue; 
    }
    
    if(x==4) 
    { if( (r==4 && c==4) || (r==4 && c==3 ) || (r==3 && c==4) ) 
      cout<<"Case #"<<o+1<<": "<<"GABRIEL"<<endl  ; 
      else cout<<"Case #"<<o+1<<": "<<"RICHARD"<<endl  ; 
      continue ; 
    }
                     
 }
   
   return 0  ; 
}
  