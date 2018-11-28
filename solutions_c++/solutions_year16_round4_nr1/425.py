#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
#include <vector>
#define all(x) x.begin() , x.end()
#define fi first
#define se second
#define pb push_back
#define umax( x , y ) x = max( x , (y) )
#define umin( x , y ) x = min( x , (y) )
#define For( i , a ) for(int i=1;i<=a;i++)
#define ort (b+s)/2
#define y2 asrwjaelkf
#define y1 asseopirwjaelkf
#define set multiset

using namespace std;

inline int read() {
	int res = 0 ;int neg ;
	while(true){char ch = getchar();if(ch>='0' && ch<='9' || ch=='-'){if(ch=='-') neg = -1;else neg = 1 , res = ch-'0';break;} }
	while(true){char ch = getchar();if(ch>='0' && ch<='9') res*=10 , res+=ch-'0';else break;}
	return res*neg;
}


typedef long long Lint;
typedef double db;
typedef pair<int,int> ii;
typedef pair<db,db> dd;
typedef pair<ii,int> iii;
typedef pair<ii,ii> i4;

const int maxn = 2020;
const int maxm = 1000020;
const int MOd = 1e9 + 7;
const int K = 320;

int a, b, c, d;
string s;
string dn[260][20];

string f( char c, int a ) {
	string s;
	s += c;
	if( a == 0 ) return s;
	if( dn[c][a].size() ) return dn[c][a];
	string s1;
	string s2;
	
	if( c == 'R' ) s1 = f( 'R', a-1 ), s2 = f( 'S', a-1 );
	if( c == 'S' ) s1 = f( 'S', a-1 ), s2 = f( 'P', a-1 );
	if( c == 'P' ) s1 = f( 'P', a-1 ), s2 = f( 'R', a-1 );
	if( s1 > s2 ) swap( s1, s2 );
	return dn[c][a] = s1 + s2;
}

bool look( string s ) {
	int t1 = 0, t2 = 0, t3 = 0;
	for(int i=0;i<s.size();i++) {
		if( s[i] == 'R' ) t1++;
		if( s[i] == 'P' ) t2++;
		if( s[i] == 'S' ) t3++;
	}
	if( t1 == b && t2 == c && t3 == d ) {
		cout << s << endl;
		return 1;
	}
	return 0;
}

void solve() {
	
	scanf("%d %d %d %d",&a,&b,&c,&d);
	string s1 = f( 'P', a );
	string s2 = f( 'R', a );
	string s3 = f( 'S', a );
	//~ cout << s1 << endl;
	//~ cout << s2 << endl;
	if( look( s1 ) ) return;
	if( look( s2 ) ) return;
	if( look( s3 ) ) return;
	printf("IMPOSSIBLE\n");
}

int main() {
	
	int n;
	scanf("%d",&n);
	int cnt = 0;
	while( n-- ) {
		printf("Case #%d: ",++cnt);
		solve();
	}
	
	return 0;
}
