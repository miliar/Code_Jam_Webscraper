#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i ) 
#define Maxn 105
#define Maxm 105
#define Inf (~0U >> 1 )

const int go[5][2] = {0,0, -1,0, 0,1, 1,0, 0,-1 } ;

/*int n, m, ans, Ccheck, T, Case, ANS ;
int vis[Maxn][Maxm], map[Maxn][Maxm], tmap[Maxn][Maxm] ;
bool circle[Maxn][Maxm] ;

inline int Check( int x, int y )  // 检查(x,y)走会不会死 
{
	int re = 1, direc = map[x][y] ;
	++ Ccheck ;	
	while(true) {
		if(vis[x][y] == Ccheck) return 0 ; // 有个环
		vis[x][y] = Ccheck ;
		x += go[direc][0] ;
		y += go[direc][1] ;
		if((x<1) || (x>n) || (y<1) || (y>m)) return re ; //会死
		if(map[x][y]) {
			direc = map[x][y] ;
			++ re; 
		}
	}
}

inline void Do_circle( int x, int y )
{
	int direc = map[x][y];
	while(true) {
		if(circle[x][y]) return ;
		circle[x][y] = true ;
		x += go[direc][0] ;
		y += go[direc][1] ;
		if(map[x][y]) direc = map[x][y] ;
	}
}

inline void ChangeDirection( int x, int y ) 
{
	int direc = map[x][y];
	while(true) {
		if(circle[x][y]) return ;
		circle[x][y] = true ;
		x += go[direc][0] ;
		y += go[direc][1] ;
		if(map[x][y]) {
			if(direc&1)
				map[x][y] = 4-direc ;
			else 
				map[x][y] = 6-direc ;
			return ;
		}
	}
}

inline bool ChangeSingle( int x, int y ) // 途径0个箭头 
{
	int re = 0, rei, direc, p, i ;
	
	direc = map[x][y] ;
	rep( i, 1, 4 ) {
		if( direc == i ) continue ;
		map[x][y] = i ;
		p = Check(x,y) ;
		if(p == 1) continue ;
		if(p == 0) {
			re = 1; rei = i; break ;	
		}
		else { 
			re = 2 ;rei = i;
		}
	}
	if(!re) return false ;
	ans += re ;
	map[x][y] = rei ;
	if(re == 2) 
		ChangeDirection(x, y) ;
	else 
		Do_circle(x, y) ;
	return true ;
}


inline int Calc()
{
	int i, j, p ;
	
	ans = Ccheck = 0 ;
	memset( vis, 0, sizeof( vis ) ) ;
	memset( circle, 0, sizeof( circle ) ) ;
	
	rep( i, 1, n )
		rep( j, 1, m ) 
			if((map[i][j]) && (!circle[i][j])) {
				p = Check(i, j) ;
				if(!p) { // 有个环 
					Do_circle(i, j) ;
				} else { // p=途径数量
					if(p == 1) { 
						if(ChangeSingle( i, j )) ;
						else {
							return Inf ; 
						}
					} else {
						ChangeDirection(i, j) ;	
						++ ans ;
					}
				}		
			}	
	return ans ;
}

int main()
{
	int i, j ;
	char ch ;
	
	freopen("input.txt","r",stdin) ;
	freopen("output.txt","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		ANS = Inf ;
		memset( map, 0, sizeof( map ) ) ;
		memset( tmap, 0, sizeof( tmap ) ) ;
		
		scanf("%d%d", &n, &m);
		rep( i, 1, n ) {
			scanf("\n") ;
			rep( j, 1, m ) {
				scanf("%c", &ch) ;
				if( ch == '>' ) 
					map[i][j] = 2 ;
				else if( ch == '<' )
					map[i][j] = 4 ;
				else if( ch == 'v' )
					map[i][j] = 3 ;
				else if( ch == '^' )
					map[i][j] = 1 ;
			}
		}
		
		ANS = min( ANS, Calc()) ;
		
		rep( i, 1, n )
			rep( j, 1, m )
				tmap[j][i] = map[i][j] ;
		memcpy( map, tmap, sizeof( map ) ) ;
		swap( n, m ) ;
		ANS = min( ANS, Calc()) ;
			
		if( ANS == Inf ) 
			printf("Case #%d: IMPOSSIBLE\n", ++Case) ;
		else 
			printf("Case #%d: %d\n", ++Case, ANS) ;
	}
	return 0 ;	
}
*/

int n, m, ans, Ccheck, T, Case ;
int map[Maxn][Maxm], vis[Maxn][Maxm] ;

inline int Check( int x, int y )  // 检查(x,y)走会不会死 
{
	int re = 1, direc = map[x][y] ;
	++ Ccheck ;	
	while(true) {
		if(vis[x][y] == Ccheck) return 0 ; // 有个环
		vis[x][y] = Ccheck ;
		x += go[direc][0] ;
		y += go[direc][1] ;
		if((x<1) || (x>n) || (y<1) || (y>m)) return re ; //会死
		if(map[x][y]) {
			direc = map[x][y] ;
			++ re; 
		}
	}
}

inline int Sum( int x, int y ) 
{
	int re = 0, i ;
	rep( i, 1, m ) 
		if((map[x][i]) && (i!=y) )
			++ re ;
	rep( i, 1, n ) 
		if((map[i][y]) && (i!=x) )
			++ re ;
	return re; 	
}

bool Check_possible()
{
	int i, j ; 
	
	rep( i, 1, n ) 
		rep( j, 1, m ) 
			if( map[i][j] ) 
				if( Sum(i, j ) == 0 )
					return false ;		
	return true ;
}

int main()
{
	int i, j, p ;
	char ch ;
	
	freopen("A-large.in","r",stdin) ;
	freopen("output.txt","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		memset( map, 0, sizeof( map ) ) ;
		memset( vis, 0, sizeof( vis ) ) ;
		ans = Ccheck = 0 ;
		
		scanf("%d%d", &n, &m) ;
		rep( i, 1, n ) {
			scanf("\n") ;
			rep( j, 1, m ) {
				scanf("%c", &ch) ;
				if( ch == '>' ) 
					map[i][j] = 2 ;
				else if( ch == '<' )
					map[i][j] = 4 ;
				else if( ch == 'v' )
					map[i][j] = 3 ;
				else if( ch == '^' )
					map[i][j] = 1 ;	
			}
		}
		
		if( Check_possible() ) {
			rep( i, 1, n ) 
				rep( j, 1, m )
					if( map[i][j] ) {
						p = Check( i, j ) ;
						if(p == 1) ++ ans ;			
					}
			printf("Case #%d: %d\n", ++Case, ans) ;
		} else 
			printf("Case #%d: IMPOSSIBLE\n", ++Case) ;
	}
	return 0 ;	
}
