#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include <limits>
   
using namespace std;
  
long long gcd( long long b, long long s ){
    return (s!=0) ? gcd( s, b%s ) : b;
}
  
long long Pow( long long a, long long b, long long c ){
    if( b == 0 ) return 1%c;
    else if( b == 1 ) return a%c;
    else{
        long long A = Pow( a, b/2, c );
        A = (A*A) % c;
        if( b & 1 ) A = (A*a) % c;
        return A;
    }
}

const long long INF = 1e9 + 7;
const long long INF9 = 1e9 + 9;
typedef pair <int, int> ii;

char s[105][105];
int dx[] = { 1, -1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };

int dir( char k ){
	if( k == '^' ) 
		return 1;
	else if( k == 'v' )
		return 0;
	else if( k == '>' )
		return 2;
	else if( k == '<' ) 
		return 3;
	return -1;
}

bool check( int x, int y, int r, int c ){

	bool ok = 0;
	for(int k=0; k<4; k++){
		int cx = x + dx[k], cy = y + dy[k];
		while( 0 <= cx && cx < r && 0 <= cy && cy < c ){
			if( s[cx][cy] != '.' ) {
				return 1;
				break;
			}
			cx += dx[k], cy += dy[k];

		}
	}
	return 0;
}

bool v[105][105];

int go( int x, int y, int r, int c ){
	
	if( v[x][y] ) return 0;
	int k = dir( s[x][y] );
	v[x][y] = 1;

	int cx = x+dx[k], cy = y+dy[k];
	bool ok = 0;
	while( 0 <= cx && cx < r && 0 <= cy && cy < c ){
		if( s[cx][cy] != '.' ){
			ok = 1;
			break;
		}
		cx += dx[k], cy += dy[k];
	}
	if( ok ) return go( cx, cy, r, c );
	return 1;
}

void solve(){
	int r, c;
	scanf("%d %d", &r, &c);

	for(int i=0; i<r; i++)
		scanf("%s", s+i);
	bool ok = 1;
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if( s[i][j] != '.' && !check( i, j, r, c ) )
				ok = 0;
			v[i][j] = 0;
		}
	}
	if( ok ){
		int ans = 0;
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				if( s[i][j] != '.' && !v[i][j] ){
					ans += go( i, j, r, c );
				}
			}
		}
		printf("%d\n", ans);
	}else
		puts("IMPOSSIBLE");
}

int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve();
	}
}