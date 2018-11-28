#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll cal( int id , int K , int C )
{
	ll res = id;
	for( int i = 0 ; i < C - 1 ; i++ )
		res = 1ll * (res - 1) * K + id;
	return res;
}
int main()
{
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("D_small.out","w",stdout);
	
	int T , K , C , S;
	scanf( "%d",&T );
	for( int i = 1 ; i <= T; i++ )
	{
		scanf( "%d%d%d",&K,&C,&S ); 
		cout << "Case #" << i << ": ";
		if( S < K )
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		for( int j = 1 ; j <= K ; j++ )
			cout << j << " ";
		cout << endl;
	}
	return 0;
}
