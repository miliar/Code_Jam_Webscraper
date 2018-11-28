#include <algorithm>
#include <bitset>
#include <deque>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
#include <vector>
#include <ctime>
 
#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define clr(a, v) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cout << #x << ": " << x << endl;
#define trace2(x, y) cout << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define read ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 
using namespace std;
 
typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;
typedef pair<ii,int> tri;



string S[5];
int H[5][5], HH[5][5];



int main(){
    int n;
    long long int m;
    int T,caso=1;
    
    cin>>T;
    while(T--){
        cin>>n;
        FOR(i,n)cin>>S[i];
        
        FOR(i,n)FOR(j,n) if(S[i][j]=='1') H[i][j]=1; else H[i][j]=0;
                          
        vii L;         
        FOR(i,n)FOR(j,n) if(H[i][j] == 0){
            L.pb(mp(i,j));                
        }         
                        
        
        int ans=16;
                        
        FOR(k,1<<L.sz){
        
            FOR(i,n)FOR(j,n) HH[i][j]=H[i][j];
            
            FOR(j,L.sz)if( k &(1<<j)){
                HH[L[j].fst][L[j].snd] = 1;        
            }  
            
            //printf("checko %d\n",k);
            //FOR(i,n){ FOR(j,n)printf("%d",HH[i][j]); printf("\n"); }    
            int ok=1;
            int tot = 0;
            
            FOR(i,n)FOR(j,n) if( ok and HH[i][j] ){
                vi f,c;
                FOR(p,n) if(HH[i][p]==1) c.pb(p); 
                FOR(p,n) if(HH[p][j]==1) f.pb(p);
                
                if(c.sz!=f.sz)           ok=0;
                
                FOR(ii,n)FOR(jj,n){
                    int coin = (find( all(c), jj )!=c.end()) + (find( all(f), ii )!=f.end());
                    //printf("coin %d\n",coin);
                    if(coin==2 and HH[ii][jj]==0) ok=0;
                    if(coin==1 and HH[ii][jj]==1) ok=0;
                } 
                
                if(!ok) break;    
                
                tot+=c.sz;
                
                FOR(ii,f.sz)FOR(jj,c.sz){
                    HH[ f[ii] ][ c[jj] ] = 0;
                }
                     
            }
            
            if(tot!=n) ok=0;
            
            
            if(ok){
                ans = min(ans, __builtin_popcount(k));
                //printf("ok %d\n",ans);;
                
            }
        }
        
        printf("Case #%d: %d\n",caso++,ans);                        
    }    
    

    return 0;
}




