#include <cstdio>
#include <algorithm>
using namespace std;

int n ; 
double A[2000] , B[2000] ; 

bool cmp( double  x , double  y ){
	return x < y ; 	
}

int main(){
	int T , CASE = 0;;
	scanf("%d",&T ) ; 
	while( T-- ){
		scanf("%d",&n) ; 
	
		for(int i=0;i<n;++i)
			scanf("%lf",&A[i] ) ; 
		
		for(int i=0;i<n;++i)
			scanf("%lf",&B[i]);
		
		sort( A , A+n , cmp ) ; 
		sort( B , B+n , cmp ) ;
		
		
		/*
		for(int i=0;i<n;++i)
			printf("%d ",A[i]);
		printf("\n");
		 */
		
		int a = 0  ; 
		int head1 = 0 , head2 = 0 ;
		int back1 = n , back2 = n  ;
		while( head2 < back2 && head1 < back1 ){
			if( A[head1] < B[head2] ){
				
				back2-- , head1++; 
			}
			else if( A[head1] == B[head2] ){	
				while( head2 < back2 && head1 < back1 ){
					if( A[back1-1] > B[back2-1] )
						a++ , back1-- , back2-- ; 
					else{
						if( A[head1] < B[back2-1] ) ;
						head1++ , back2-- ;
						break;
					}
				}
			}
			
			else{
				a++ ; 
				head1++ , head2++ ; 	
			}
		}	
		
		//-------------------------------
		for(int i=0;i<n;++i)	swap(  A[i] , B[i] );
		int  b = 0 ;
		head1 = 0 , head2 = 0 ;
		back1 = n , back2 = n  ;
		while( head2 < back2 && head1 < back1 ){
			if( A[head1] < B[head2] ){
				back2-- , head1++; 
				b++ ;
			}
			else if( A[head1] == B[head2] ){	
				while( head2 < back2 && head1 < back1 ){
					if( A[back1-1] > B[back2-1] )
						back1-- , back2-- ; 
					else{
						if( A[head1] < B[back2-1] )	b++ ;
						head1++ , back2-- ;
						break;
					}
				}
			}
			
			else{
				head1++ , head2++ ; 	
			}
		}
		
		printf("Case #%d: %d %d\n",++CASE,a,b);

	}
	return 0; 	
}
