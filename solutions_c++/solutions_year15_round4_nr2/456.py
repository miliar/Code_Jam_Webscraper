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

#define	eps	1e-5
#define	sifir( aa )	( abs(aa)<eps )
#define	esit( aa,bb )	( sifir( (aa)-(bb) ) )

using namespace std;

int	n;
double	v,r;
double	v1,r1,v2,r2;
int	cnt;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int	t,id=0;
	cin >> t;
	while( t-- ){
		cin >> n >> v >> r;
		go:;
		if( n==1 ){
			cin >> v1 >> r1;
			if( !esit( r,r1 ) )	printf("Case #%d: IMPOSSIBLE\n",++id),cnt++;
			else	printf("Case #%d: %.12lf\n",++id,v/v1);
			continue;
		}
		cin >> v1 >> r1 >> v2 >> r2;
		if( esit( r1,r2 ) ){
            if( !esit( r,r1 ) )	printf("Case #%d: IMPOSSIBLE\n",++id),cnt++;
			else	printf("Case #%d: %.12lf\n",++id,v/(v1+v2));
			continue;
		}
		if( r1>r and r2>r or r1<r and r2<r ){
			printf("Case #%d: IMPOSSIBLE\n",++id),cnt++;
			continue;
		}
		if( r1<r2 ){
			swap( r1,r2 );
			swap( v1,v2 );
		}
		assert( !esit( r1,r2 ) );
		int	ok = 0;
		double	res = 0;
		double	i = v*(r-r2)/(r1-r2);
		if( esit( (i*r1+(v-i)*r2)/v,r ) )
			{
				ok = 1;
				res = max( i/v1,(v-i)/v2 );
			}
		if( esit( i,v ) )	cerr << i << " " << v << endl;
		if( !ok )	printf("Case #%d: IMPOSSIBLE\n",++id),cnt++;
		else	printf("Case #%d: %.12lf\n",++id,res);
	}
	cerr << cnt << endl;
}
