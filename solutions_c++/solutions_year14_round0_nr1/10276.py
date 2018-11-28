#include <stdio.h>
int B[20] ;
int L[4] ;
int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int T ;	
	scanf("%d",&T);
	for( int i = 0 ; i < T ; i++ )
	{
		int a , soluzione = 0 , count = 0 , first = 0 ;
		scanf("%d",&a);
		for( int j = 0 ; j < 20 ; j++ ) B[j] = 0 ;
		for( int j = 0 ; j < a-1 ; j++ ) scanf("%d %d %d %d",L,L+1,L+2,L+3);
		scanf("%d %d %d %d",L,L+1,L+2,L+3);
		
		for( int j = 0 ; j < 4 ; j++ ) B[L[j]] = 1 ;		
		for( int j = a ; j < 4 ; j++ ) scanf("%d %d %d %d",L,L+1,L+2,L+3);	
		scanf("%d",&a);
		for( int j = 0 ; j < a-1 ; j++ ) scanf("%d %d %d %d",L,L+1,L+2,L+3);
		scanf("%d %d %d %d",L,L+1,L+2,L+3);	
		
		for( int j = 0 ; j < 4 ; j++ ) if( B[L[j]] == 1 ){ count++; first = L[j] ; }	
		soluzione = (count == 0) ? 0 : ( count == 1 ? first : -1 );
		
		for( int j = a ; j < 4 ; j++ ) scanf("%d %d %d %d",L,L+1,L+2,L+3);	
			 if( soluzione == 0 ) 	printf("Case #%d: Volunteer cheated!\n",i+1);
		else if( soluzione == -1 )	printf("Case #%d: Bad magician!\n",i+1);
		else						printf("Case #%d: %d\n",i+1,soluzione);	
	}
}
