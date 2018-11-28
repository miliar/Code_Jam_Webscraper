#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std ;

bool num[17] ;
int T ;
int tag ;

int main()
{
	freopen("A.in","r",stdin) ;
	freopen("A.out","w",stdout) ;
	int i , j , k , l , p , ans ;
	while( cin>>T ) {
		for( i = 1 ; i <= T ; i ++ ) {
			memset(num,false,17) ;
			cin>>j ;
			tag = 0 ;
			for( k = 1 ; k <= 4 ; k ++ ) {
				for( l = 1 ; l <= 4 ; l ++ ) {
					cin>> p ; 
					if( k == j ) num[p] = true ;
				}
			}
			cin>>j ;
			for( k = 1 ; k <= 4 ; k ++ ) {
				for( l = 1 ; l <= 4 ; l ++ ) {
					cin>> p ; 
					if( k == j && num[p] ) {
						tag ++ ;
						ans = p ;
					}
				}
			}
			if( tag == 0 ) 
				printf("Case #%d: Volunteer cheated!\n",i);
			else if( tag > 1 ) 
				printf("Case #%d: Bad magician!\n",i);
			else
				printf("Case #%d: %d\n",i,ans);
		}
	}

	return 0 ;
}