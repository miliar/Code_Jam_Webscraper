#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <iostream>

using namespace std ;

struct Point {
	int x, y;
	Point() {}
	Point( int a, int b ) {x=a, y=b;}

	Point operator - ( Point &b ) {
		return Point(x-b.x, y-b.y);
	}
};

double det( Point a, Point b ) {
	return a.x*b.y - a.y*b.x ;
}
double dot( Point a, Point b ) {
	return a.x*b.x + a.y*b.y ;
}
const int MAXN = 201 ;
const int inf = 10000000 ;
char a[MAXN][MAXN] ;
int dir[1000] ;
int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
int n , m ;

bool inside( int x , int y ) {
	return x >= 0 && x < n && y >= 0 && y < m ;
}

int main() {

	dir['<'] = 1 ;
	dir['>'] = 0 ;
	dir['^'] = 2 ;
	dir['v'] = 3 ;

	int T ;
	cin >> T ;
	while ( T-- ) {
		cin >> n >> m ;
		
		
		for ( int i = 0 ; i < n ; ++i ) {
			for ( int j = 0 ; j < m ; ++j ) {
				cin >> a[i][j] ;
			}		
		}
		
		int ans = 0 ;

		for ( int i = 0 ; i < n ; ++i ) {
			for ( int j = 0 ; j < m ; ++j ) {
				if ( a[i][j] != '.' ) {
					int l = dir[ a[i][j] ] ;
					
					bool flag = false ;
					for ( int k = 1 ; ; ++k ) {
						int xx = i + dx[l] * k ;
						int yy = j + dy[l] * k ;
						if ( !inside(xx,yy) )
							break;
						if ( a[xx][yy] != '.' ) {
							flag = true ;
							break;
						}
						
					}
					if ( !flag ) {
						bool f = true ;
						for ( int l = 0 ; l < 4 ; ++l ) {
							for ( int k = 1 ; f ; ++k ) {
								int xx = i + dx[l] * k ;
								int yy = j + dy[l] * k ; 
								if ( !inside(xx,yy) ) break;
								if ( a[xx][yy] != '.' ) {
									++ans ;
									f = false ;
									break;
								}
							}
						}
						if ( f )
							ans = inf ;
					}

				}
			}
		}
		static int test = 1;
		printf("Case #%d: ",test++);
		if ( ans < inf )
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
