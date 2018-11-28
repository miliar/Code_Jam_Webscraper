#include <bits/stdc++.h>
using namespace std;
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fr(i,a,b) for(int i = (a); i >= (b); i--)
#define rep( i , n ) for( int i = 0 ; i < n ; i++ )
#define repi( n , i ) for( int i = n ; i >= 0 ; i-- )
#define sc( x ) scanf( "%d" , &x )
#define sc2( x , y ) scanf( "%d%d" , &x , &y )
#define sc3( x , y , z) scanf( "%d%d%d" , &x , &y , &z)
#define pf( x ) printf( "%d\n" , x )
#define pfd( x ) printf( "%.9f\n" , x )
#define all( v ) v.begin(),v.end()
#define all_r( v ) v.rbegin() , v.rend()
#define fi first
#define se second
#define SZ(a) int(a.size())
#define pb push_back
#define pi acos(-1.0)
#define EPS (int)( 1e-6 )
#define MCM( a , b ) ( ( a*b )/( __gcd( a , b ) ) )
typedef double db ;
typedef long double ld ;
typedef long long ll ;
typedef vector<int> vi ;
typedef vector<vi> vvi ;
typedef vector<ll> vl ;
typedef vector<bool> vb ;
typedef pair<int,int> pii ;
typedef vector<pii> vii ;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t; sc(t); 
	rep(i,t){
		char m[101]; int x=0,a,b;
		cin>>m;b=(m[0]=='+'?1:0);
		rep(j,strlen(m)){
			a=(m[j]=='+'?1:0);
			if(a!=b)x++;
			b=a;
		}
		if(a==0)x++;
		cout<<"Case #"<<i+1<<": "<<x<<endl;
	}
}

