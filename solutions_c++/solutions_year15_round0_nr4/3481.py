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
{ int t ;  
  
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
      
    
    
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    










