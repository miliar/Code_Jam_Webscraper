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


float P[205];
float S[205];
float aux[205];

int M[205];

int main(){
    
    int T,n,m,caso=1;
    cin>>T;
    
    while(T--){
        cin>>n>>m;
        
        FOR(i,n) cin>>P[i];    
        
        float ans=0;
        FOR(i,n) M[i]=0;
        FOR(i,m) M[n-i-1] = 1;
        
        do{
            FOR(i,m+1) S[i]=0.0;
            S[0]=1.0;
            FOR(i,n)if(M[i]){
                FOR(j,m+1) aux[j] = 0;
                FOR(j,m+1){
                    if(j>=1) aux[j] += S[j-1]*P[i];
                    aux[j] += S[j]*(1-P[i]);
                    //printf("%.10lf\n",aux[j]);
                } 
                FOR(j,m+1) S[j] = aux[j];

            }
            
            ans = max(ans, S[m/2]);            
            
        }while(next_permutation(M,M+n));      
        
        printf("Case #%d: %.10lf\n",caso++,ans);                    
    }    
    

    return 0;
}




