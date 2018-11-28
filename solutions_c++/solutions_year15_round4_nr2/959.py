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
#define read ios::sync_with_stdio(false)

using namespace std;

typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

double EPS = 1e-9;

int cmp(double a, double b){
    return (a+EPS<b)?-1:(a-EPS>b)?1:0;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    int cas = 1;

    while(T--){
        int N;
        double V,T,C,R;
        cin>>N>>V>>T;
        double izq = 0.0, der=0.0,cent=0.0;
        double rizq = 0.0, rder=0.0,rcent=0.0;
        FOR(i,N){
            cin>>R>>C;
            if ( cmp(C,T)<0 ) {
                izq+=(R*(T-C));
                rizq+=R;
            }
            else if (cmp(C,T)>0) {
                der+= (R* (C-T) ) ;
                rder+=R;
            }
            else {
                cent+=(R*C);
                rcent+=R;
            }
        }
        //trace2(rder,rizq);
        if (cmp( rcent,0.0 ) !=0 ) {
            printf("Case #%d: %.7lf\n",cas,V/rcent);
        }
        else if ( cmp( der,0.0 ) == 0 or cmp(izq,0.0) ==  0 ){
            printf("Case #%d: IMPOSSIBLE\n",cas);
        }
        else{
            double t1 = 1.0, t2 = izq/der;
            double V1 = rizq + rder*t2;
            printf("Case #%d: %.7lf\n",cas,max(1.0,t2)*V/V1);
        }
        cas++;
    }
}
