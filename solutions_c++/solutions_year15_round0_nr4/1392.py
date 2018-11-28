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

#define	G	{cout << "GABRIEL" << endl;continue;}
#define	R	{cout << "RICHARD" << endl;continue;}

using namespace std;

int	main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int	t,id=0;
	cin >> t;
	while( t-- ){
		printf("Case #%d: ",++id);
		int	r,c,x;
		cin >> x >> r >> c;
		if( r>c )	swap( r,c );
		if( x==1 ){
			G;
		}
		if( x==2 ){
			if( r*c%2==0 )	G;
			R;
		}
		if( x==3 ){
			if( r*c%3 or r*c<3 )	R;
			if( r==1 and c==3 )	R;
			G;
		}
		if( x==4 ){
			if( r*c%4 or r*c<4 )	R;
			if( r==1 and c==4 )	R;
			if( r==2 and c==2 )	R;
			if( r==2 and c==4 )	R;
			if( r==3 and c==4 ) G;
			if( r==4 and c==4 ) G;
		}
		assert(0);
	}

}
