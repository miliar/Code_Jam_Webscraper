#include <bits/stdc++.h>

#define	st first
#define	nd second
#define	mp make_pair
#define	pb push_back
#define	lli long long int
#define	all( gg )	gg.begin(),gg.end()
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	FP( ii,aa,bb ) for( lli ii=aa;ii<=bb;ii++ )
#define	FM( ii,aa,bb ) for( lli ii=aa;ii>=bb;ii-- )
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;

#define	mod	1000000007LL

using namespace std;

int	m,n;
char	s[200][200];
int		can[200][200][10];

int	ctrl( int x,int y ){
	return	1<=x and x<=m and 1<=y and y<=n;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int	t,id=0;
	cin >> t;
	while( t-- ){
		cin >> m >> n;
		FP( i,1,m )
			cin >> s[i]+1;
		memset( can,1,sizeof can );
		FP( i,1,m )
			FP( j,1,n ){
				if( i==1 ){
                    int x = i;
                    int y = j;
                    while( ctrl( x,y ) and s[x][y]=='.' )	x++;
                    if( ctrl( x,y ) )	can[x][y][0] = 0;
				}
				if( i==m ){
                    int x = i;
                    int y = j;
                    while( ctrl( x,y ) and s[x][y]=='.' )	x--;
                    if( ctrl( x,y ) )	can[x][y][1] = 0;
				}
				if( j==1 ){
                    int x = i;
                    int y = j;
                    while( ctrl( x,y ) and s[x][y]=='.' )	y++;
                    if( ctrl( x,y ) )	can[x][y][2] = 0;
				}
				if( j==n ){
                    int x = i;
                    int y = j;
                    while( ctrl( x,y ) and s[x][y]=='.' )	y--;
                    if( ctrl( x,y ) )	can[x][y][3] = 0;
				}
			}
		int	res=0,ok=1;
		FP( i,1,m )
			FP( j,1,n ){
				if( !can[i][j][0] and !can[i][j][1] and !can[i][j][2] and !can[i][j][3] ){
					ok = 0;
					break;
				}
				if( s[i][j]=='^' and !can[i][j][0] )	res++;
				if( s[i][j]=='v' and !can[i][j][1] )	res++;
				if( s[i][j]=='<' and !can[i][j][2] )	res++;
				if( s[i][j]=='>' and !can[i][j][3] )	res++;
			}
		if( !ok )	printf("Case #%d: IMPOSSIBLE\n",++id);
		else	printf("Case #%d: %d\n",++id,res);
	}
}
