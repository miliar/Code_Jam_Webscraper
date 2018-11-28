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

int N,M;
string s[105];

int f(int x, int y){
    char able [4];
    FOR(i,4) able[i] = '.';
    for(int i = x-1; i>=0 and able[0]=='.';i--) if( s[i][y] !='.' ) able[0] = s[i][y];
    for(int i = x+1; i< N and able[1]=='.';i++) if( s[i][y] !='.' ) able[1] = s[i][y];
    for(int i = y-1; i>=0 and able[2]=='.';i--) if( s[x][i] !='.' ) able[2] = s[x][i];
    for(int i = y+1; i< M and able[3]=='.';i++) if( s[x][i] !='.' ) able[3] = s[x][i];

    if ( able[0] =='.' and able[1] =='.' and able[2] =='.' and able[3] =='.' ) return -100000000;

    if (s[x][y] == '^')
        if (able[0]=='.') return 1;
        else              return 0;

    if (s[x][y] == 'v')
        if (able[1]=='.') return 1;
        else              return 0;

    if (s[x][y] == '<')
        if (able[2]=='.') return 1;
        else              return 0;

    if (s[x][y] == '>')
        if (able[3]=='.') return 1;
        else              return 0;

}

int main(){
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    int cas = 1;

    while(T--){
        int ans = 0;
        cin>>N>>M;
        FOR(i,N) cin>>s[i];
        FOR(i,N) FOR(j,M)
            if(s[i][j] != '.') ans+=f(i,j);
        if (ans>=0) printf("Case #%d: %d\n",cas,ans);
        else        printf("Case #%d: IMPOSSIBLE\n",cas);
        cas++;
    }
}
