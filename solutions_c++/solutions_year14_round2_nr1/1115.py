#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

int  point[105];
char str[105][105];
int  len[105];
int  mid[105][105];
int  tem[105];

int main()
{
	int T,N,i,j,t;
	while ( ~scanf("%d",&T) )
	for ( t = 1 ; t <= T ; ++ t ) {
		scanf("%d",&N);
		for ( i = 0 ; i < N ; ++ i )
			scanf("%s",str[i]);
			
		memset( point, 0 , sizeof(point) );
		for ( i = 0 ; i < N ; ++ i )
			len[i] = strlen(str[i]);
		
		int  flag_e,flag_c,count,deep = 0;
		char temp;
		while ( 1 ) {
			flag_e = 1;
			for ( i = 0 ; i < N ; ++ i )
				if ( point[i] != len[i] ) {
					flag_e = 0;break;
				}
			if ( flag_e ) break;
			
			flag_c = 0;
			temp = str[0][point[0]];
			for ( i = 0 ; i < N ; ++ i ) {
				count = 0;
				while ( str[i][point[i]] == temp ) {
					count ++;
					point[i] ++;
				}
				if ( count == 0 ) {
					flag_c = 1;break;
				}
				mid[i][deep] = count;
			}
			if ( flag_c ) break;
			
			deep ++;
		}
		
		printf("Case #%d: ",t);
		if ( flag_c ) printf("Fegla Won\n");
		else {
			int Mid = 0,Sum = 0;
			for ( j = 0 ; j < deep ; ++ j ) {
				for ( i = 0 ; i < N ; ++ i )
					tem[i] = mid[i][j];
				sort( tem, tem+N );
				Mid = tem[N/2];
				for ( i = 0 ; i < N ; ++ i )
					Sum += abs( Mid-tem[i] );
				
			}
			printf("%d\n",Sum);
		}
	}
	
	return 0;
}
