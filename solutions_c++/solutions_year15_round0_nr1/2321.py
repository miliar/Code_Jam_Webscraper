#include <bits/stdc++.h>

#define	FP( ii,aa,bb ) for( int ii=aa;ii<=bb;ii++ )

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
