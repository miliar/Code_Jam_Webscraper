#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
#include<climits>
#include<set>
#include<deque>
#include<queue>
#include<map>
#include<climits>
#include<string>
#include<stack>
#include<sstream>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<30)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int> 
#define mp(a,b) make_pair(a,b)
#define Q(x) (x) * (x)
#define L(x) ((x<<1) + 1)
#define R(x) ((x<<1) + 2)
#define M(x,y) ((x+y)>>1)
#define fi first
#define se second
#define MOD 10009
#define N 5

string s[N];

int dx[4] = { 1 , 0 , 1 , 1 };
int dy[4] = { 0 , 1 , 1 , -1 };

bool f(int x,int y,char c){
    //if( x == 0 && y == 0 ) cout << x << " " << y << " " << c << endl;
    for(int k = 0 ; k < 4 ; k++){
        bool ok = 1;
        for(int i = 0 ; i <= 3 ; i++){
            int nx = x + dx[k] * i , ny = y + dy[k] * i;
            //if( x == 0 && y == 0 && c == 'X' ) cout << nx << " " << ny << endl;
            if( nx < 4 && nx >= 0 && ny < 4 && ny >= 0 ){
                if( s[nx][ny] == c || s[nx][ny] == 'T' ){}
                else ok = 0;
            }
            else ok = 0;
        }
        //if( x == 0 && y == 0 && c == 'X' )  cout << ok << endl;
        if(ok) return 1;
    }
    return 0;
}

int main(){
    int tc;
    sc(tc);
    for(int test = 1 ; test <= tc ; test++){
        for(int i = 0 ; i < 4 ; i++)
            cin >> s[i];
            
        bool Xwin = 0 , Owin = 0 , F = 0;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++){
                if( s[i][j] == '.' ) F = 1;
                if( s[i][j] == 'X' && f( i , j , s[i][j] ) ) Xwin = 1;
                if( s[i][j] == 'O' && f( i , j , s[i][j] ) ) Owin = 1;
                if( s[i][j] == 'T' && f( i , j , 'X' ) ) Xwin = 1;
                if( s[i][j] == 'T' && f( i , j , 'O' ) ) Owin = 1;
            }
        
        printf("Case #%d: ",test);
        if( Xwin ) printf("X won");
        else if( Owin ) printf("O won");
        else if( F ) printf("Game has not completed");
        else printf("Draw");
        printf("\n");
    }
    return 0;
}
