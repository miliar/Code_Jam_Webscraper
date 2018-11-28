#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t,n,test = 1,c1,c2;
	double naomi[1010],ken[1010];
	scanf("%d",&t);
	while ( test <= t ) {
		c1 = c2 = 0;
		
		scanf("%d",&n);
		for ( int i = 0; i < n; i++ ) scanf("%lf",&naomi[i]);
		for ( int i = 0; i < n; i++ ) scanf("%lf",&ken[i]);
		
		sort(naomi,naomi+n);
		sort(ken,ken+n);

		int i,k;
		i = k = 0;

		while ( i < n && k < n ) { 
			if ( naomi[i] < ken[k] ) i++;
			else if ( naomi[i] > ken[k] ) { c1++; i++; k++; }
		}

		k = 0;
		for ( i = 0; i < n; i++ ) {
			while ( k < n && ken[k] < naomi[i] ) k++;
			if ( k == n ) {
				c2 += (n - i);
				break;
			}
			k++;
		}
		
		printf("Case #%d: %d %d\n",test,c1,c2);
		test++;
	}
	return 0;
}
