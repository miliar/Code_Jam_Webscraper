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

int	n;
char	s[1005];

char	solve( int x ){
	x += s[0]-'0';
	FP( i,1,n ){
		if( s[i]-'0' and i>x )	return	0;
		x += s[i]-'0';
	}
	return	1;
}

int	main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int	t,id=0;
	cin >> t;
	while( t-- ){
		cin >> n >> s;
		FP( i,0,n )
			if( solve(i) ){
				printf("Case #%d: %d\n",++id,i);
				break;
			}
	}
}
