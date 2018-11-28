#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std ;

#define N 1001

bool used[N] ;
double num1[N] ;
double num2[N] ;
int ans1 ; 
int ans2 ;
int T , n ;

int solve1()
{
	int max1 = n , max2 = n ;
	int minn = 1 ;
	int i , j ;
	int ans = 0 ;
	memset(used,false,n+1) ;
	for( i = 1 ; i <= n ; i ++ ) {
		if(  num1[max1] > num2[max2] ) {
			if( num1[i] > num2[minn] ) {
				minn ++ ;
				ans ++ ;
			}
			else {
				for( j = max2 - 1 ; used[j] == true && j > 0 ; j -- ) ;
				max2 = j ;
			}
		}
		else {
			for( j = minn ; num2[j] < num1[max1] || used[j] == true ; j ++ ) ;
			if( j == max2 ) {
				for( j = max2 - 1 ; used[j] == true && j > 0 ; j -- ) ;
				max2 = j ;
			}
			else used[j] = true ;
		}
	}

	return ans ;
}

int solve2()
{
	int i = 1 , j = 1 ;
	int ans = 0 ;
	while( j <= n ) {
		if( num2[j] > num1[i] ) 
			ans ++ , i ++ ;
		j ++ ;
	}

	return n - ans ;
}


int main()
{
	freopen("D1.in","r",stdin) ;
	freopen("D1.out","w",stdout) ; 
	int i , j ;
	while( cin>>T ) {
		for( i = 1 ; i <= T ; i ++ ) {
			cin>>n ;
			for( j = 1 ; j <= n ; j ++ )
				cin>>num1[j] ;
			for( j = 1 ; j <= n ; j ++ )
				cin>>num2[j] ;
			sort(num1,num1+n+1) ;
			sort(num2,num2+n+1) ;
			ans1 = solve1() ;
			ans2 = solve2() ;
			printf("Case #%d: %d %d\n",i,ans1,ans2);
		}
	}

	return 0 ;
}