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

#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define clr(a, v) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int64 i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define read ios::sync_with_stdio(false)

using namespace std;

typedef long long int64;
typedef vector <int64> vi;
typedef pair <int64,int64> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int64 MOD = 1e9+7;

int main(){
    read;
    //freopen("A.in" ,"r",stdin);
    //freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--){
        int N;
        cin>>N;
        vi V(N+1);
        string s;
        cin>>s;
        FOR(i,V.sz) V[i] = s[i]-'0';
        int act=V[0],ans=0;
        FORN(i,1,V.sz){
            if ( act<i ){
                ans+=i-act;
                act = i+V[i];
            }
            else{
                act+=V[i];
            }
        }
        cout<<"Case #"<<cas++<<": "<<ans<<endl;
    }
}
