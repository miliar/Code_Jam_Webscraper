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


int64 A[3][15];
string S[3][13];
int64 X[3];

int main(){
    
    int T,caso=1;
    int n;
    cin>>T;
    
    
    A[0][0]=1;A[1][0]=0;A[2][0]=0;
    FOR(i,13){
        A[0][i+1] = A[0][i] + A[1][i];
        A[1][i+1] = A[1][i] + A[2][i];
        A[2][i+1] = A[2][i] + A[0][i];  
        //printf("%lld %lld %lld\n",A[0][i],A[1][i],A[2][i]);
    } 
    

    while(T--){
        cin>>n;
        cin>>X[0]>>X[1]>>X[2];
        //printf("%d %lld %lld %lld\n",n,A[0][n],A[1][n],A[2][n]);
        printf("Case #%d: ",caso++);
        
        int desfase = 1000;
        FOR(i,3){
            int fue=0;
            FOR(j,3){
                //printf("%lld %lld %lld\n", X[i],X[(i+1)%3],X[(i+2)%3]);
                if( A[j][n] != X[(j+i)%3] ) fue=1;
            }
        
            if(!fue) desfase = i;
        }    
        if(desfase > 3){
            printf("IMPOSSIBLE\n");
            continue;
        }
        // A[n][j] == X[i+j]
        //R, P, S 
        
        S[0][0] = "R"; S[1][0] = "P"; S[2][0] = "S";
        
        FOR(i,12){
            FOR(j,3){
                string &a = S[j][i]; 
                string &b = S[(j+2)%3][i];
                if(a<b) S[j][i+1] = a+b;  
                else S[j][i+1] = b+a;
            }            
        }      
                 
        cout<< S[(6+desfase)%3][n] <<endl;            
    }    
    

    return 0;
}




