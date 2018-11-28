#include <stdio.h>
int first_choice;

int second_choice;
int grid_first[16];
int grid_second[16];

int capf(int *arr1, int *arr2,int *result)
{
	int ret =0;
	int n = 4;
	for ( int i = 0 ; i < 4 ; i ++ )
	{
		for ( int j = 0 ; j < 4 ; j ++ )
		{
			if (  arr1[i] == arr2[j] ) {
				*result = arr1[i];
				++ret;
			}
		}

	}

	return ret;
}


void solve(int n) 
{
	int sol;
	printf("Case #%d: " , n ) ;
	int cap = capf( &grid_first[(first_choice-1) * 4 ], &grid_second[(second_choice -1) *4 ],&sol ) ;	
	if ( cap == 0 ) {
		printf("Volunteer cheated!\n" ) ;
		return;
	}
	if ( cap == 1 ){
		printf("%d\n" , sol ) ;
		return;
	}
	
	printf("Bad magician!\n" ) ;
	return;
}

void input_grid(int *arr)
{
	for ( int i  = 0 ;i < 4 ; i ++ )
		scanf("%d %d %d %d" , arr+(4*i) , arr + ( 4* i) +1,
				 arr+(4*i)+2 , arr+(4*i)+3 );
}

void dump_grid(int *arr)
{
	for ( int i = 0 ; i < 4 ;i ++ )
		printf("%d %d %d %d\n" , arr[(4*i)], arr [ ( 4* i) +1],
				 arr[(4*i)+2] , arr[(4*i)+3] );
 
}

int main()
{
	int n;
	scanf("%d" , &n ) ;
	for ( int i = 0 ; i < n ; i ++ )
	{
		scanf("%d" , &first_choice ) ;
		input_grid(grid_first);
		//dump_grid( grid_first);
		scanf("%d" , &second_choice ) ; 
		input_grid(grid_second);
		//dump_grid( grid_second);
		solve( i+1 ) ;

	}
	return 0;
}
