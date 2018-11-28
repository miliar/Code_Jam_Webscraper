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
int	arr[1005];

int	main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int	t,id=0;
	cin >> t;
	while( t-- ){
		cin >> n;
		FP( i,1,n )
			cin >> arr[i];
		int	mini = 10000;
		FP( k,1,1000 ){
			int	p=k;
			FP( i,1,n )	p += (arr[i]-1)/k;
			mini = min( mini,p );
		}
		printf("Case #%d: %d\n",++id,mini);
	}
}
