#include <bits/stdc++.h>
#define	FP( ii,aa,bb ) for( int ii=aa;ii<=bb;ii++ )

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
