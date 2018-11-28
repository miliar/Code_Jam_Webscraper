#include <stdint.h>
#include <stdio.h>
#include <fstream>

int main( void )
{
	int i_Cases, i_Detect, ia_Presence[11], i_Digit, i_Found = 0;
	long long ll_Data, ll_ComputedData;
	FILE *file_input, *file_output;
	
	file_input = fopen( "A-large.in", "r" );
	file_output = fopen( "output_large.txt", "w" );
	if( (file_input != NULL) && (file_output != NULL) )
	{
		//do
		//{
		//	fscanf( file_input, "%d", &i_Cases );
		//}while( i_Cases != );
		
		fscanf( file_input, "%d", &i_Cases );
		if( i_Cases == 0 )
		{
			printf( "\nError in number of cases\n" );
		}
		for( int iIndex = 0; iIndex < i_Cases; iIndex++ )
		{
			//Initialize stuff here
			i_Detect = 1+2+3+4+5+6+7+8+9+10;
			ll_ComputedData = 0;
			ll_Data = 0;
			i_Found = 0;
			
			//printf( "\nExecuting case ->%d<- \n", iIndex );
			
			for( int i = 0; i < 11; i++ )
			{
				ia_Presence[i] = 0;
			}
			
			fscanf( file_input, "%lld", &ll_Data );
			
			if( ll_Data != 0 )
			{
				ll_ComputedData = ll_Data;
				while( (ll_ComputedData < 10000000000) && (i_Found == 0) )
				{
					//printf("\n Data about to compute - %lld \n", ll_ComputedData );
					long long ll_workData = ll_ComputedData;
					while( ll_workData > 0 )
					{
						i_Digit = ll_workData % 10;
						ll_workData = ll_workData / 10;
						ia_Presence[i_Digit] = 1;
					}
					i_Found = 1;
					for( int j = 0; j <= 9; j++ )
					{
						if( ia_Presence[j] == 0 )
						{
							i_Found = 0;
							break;
						}
					}
					if( i_Found == 1 )
					{
						break;
					}
					else
					{
						ll_ComputedData = ll_ComputedData + ll_Data;
					}
					//printf("\n Computed data - %lld \n", ll_ComputedData );
					//printf("\n i_Found - %d \n", i_Found );
					//getchar();
				}
				if( i_Found == 1 )
				{
					printf( "\nCase #%d: %lld", iIndex+1, ll_ComputedData );
					fprintf( file_output, "\nCase #%d: %lld", iIndex+1, ll_ComputedData );
				}
				else
				{
					printf( "\nCase #%d: INSOMNIA", iIndex+1 );
					fprintf( file_output, "Case #%d: INSOMNIA", iIndex+1 );
				}
				
			}
			else
			{
				printf( "\nCase #%d: INSOMNIA", iIndex+1 );
				fprintf( file_output, "Case #%d: INSOMNIA", iIndex+1 ); 
			}
			//printf("\n");
		}
	}
	printf("\n");
	return 0;
}
