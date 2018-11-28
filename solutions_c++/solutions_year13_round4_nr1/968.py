#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <deque>
using namespace std;

#define F first
#define S second
#define MP make_pair
#define PB push_back
#define rep( i , a , b )  for( int i = (a) ;   i <= (b) ; ++i)
#define foreach(c , itr) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); ++itr)
#define SZ(x) (int)x.size()
#define LEN(x) (int)x.length()
#define two(x) ((1)<<(x))
typedef long long int64; 

map< int,int> start; 
map< int,int> end;
map< int ,int> all;  
const int64 mod =1000002013LL; 
int main (){
    int T ; 
    int N , M ;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
     cin >> T;
     for(int Cas=1; Cas <= T; ++Cas){
        cin >> N >> M ;
        start.clear();
        end.clear() ;
        all.clear() ; 

        int64 ans1=0,ans2=0 ; 
        for(int i=0; i < M ; ++i){ 
            int u, v ,p ;
            cin >> u >> v >> p ;
            ans1 = (ans1+ 1LL* (v-u)*(N+N+1-v+u)/2%mod*p%mod) % mod ;  
            all[u]+=p;
            all[v]+=p;
            start[u]+=p;
            end[v]+=p; 
        }
        
        //vector< pair<int,int> > now;
        vector<pair<int,int> > now ; 
       // vector< pair<int,int> > vc;  
        for( map< int ,int> :: iterator it = all.begin(); it!=all.end(); ++it){ 
            if( start.find( it->first) !=start.end()) {
                    now.push_back(make_pair(it->first,start[it->first])) ; 
                
            }
         //   cout <<it->first<<endl; 
            
            if( end.find( it->first ) !=end.end()) { 
                
                int tot = end[it->first] ;
         //      cout << it->first <<" " <<tot<<endl; 
                for(int i=SZ(now)-1; i>=0 &&tot; --i){
                   // if( tot >= now[i].second){
                      int x= min(tot,now[i].second) ;    
                      tot-=x ;  
                     // cout << x<<" "<<now[i].first <<" "<<now[i].second<<endl;  
                      now[i].second-=x;
                      ans2 =( ans2 +1LL*( it->first - now[i].first)*
                          (N + N+1 - (it->first) + now[i].first ) /2%mod*x) %mod ;
         //            cout << ans2<<endl; 
                         if(now[i].second == 0)
                          now.pop_back() ;
                      
                }
           }
       }
      // cout << ans1 << " "<<ans2<<endl; 
       cout <<"Case #"<<Cas<<": "<< (( ans1 - ans2 ) %mod + mod ) % mod <<endl ;
        }
        return 0; 
     }




