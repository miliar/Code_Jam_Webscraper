#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
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

using namespace std;
typedef long long ll  ;
typedef pair<int,int> ii  ;
typedef vector<int> vi ; 
typedef unsigned long long ull ; 
typedef pair<ll,ll> ill  ; 



int main()
{ 
    
   int t ;  cin>>t ; 
   vector<ll>v ;  
   string s ; 
   
   f(o,0,t)
   {  
      v.clear() ; 
      int n ;  
      cin>>n  ; 
      
       
      
      cin>>s  ;  
      //cout<<s<<endl; 
      for(int i=0;i<=n;i++) 
      v.pb(s[i]-'0') ; 
      
      //f(i,0,n+1)
      //cout<<v[i]<<endl; 
      
      ll  maxi=0 ;
      ll last=0 ; 
      for(int i=0;i<n;i++) 
      {  last+=v[i] ; 
         maxi= max(maxi,i+1-last) ; 
      }
        
        
      printf("Case #%d: %lld\n",o+1,maxi) ; 
   }
   
   return 0  ; 
}
      
       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
             
     



























