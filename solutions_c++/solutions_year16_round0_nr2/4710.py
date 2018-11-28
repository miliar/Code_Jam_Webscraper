#include <stdint.h>
#include <stdio.h>
#include <string.h>

int main( void )
{
	FILE *file_input, *file_output;
	char ca_SignInfo[102], c_Previous;
	int i_Cases, i_Length, i_Count;

	
	//file_input = fopen( "B-small-attempt0.in", "r" );
	file_input = fopen( "B-large.in", "r" );
	//file_input = fopen( "inputfile.in", "r" );
	file_output = fopen( "output_large.txt", "w" );
	
	if( (file_input != NULL) && (file_output != NULL) )
	{
		fscanf( file_input, "%d", &i_Cases );
		
		if( i_Cases == 0 )
		{
			printf( "\nError in number of cases\n" );
		}
		for( int iIndex = 0; iIndex < i_Cases; iIndex++ )
		{
			// Init
			c_Previous = '+';
			i_Count = 0;
			
			fscanf( file_input, "%s", ca_SignInfo );
			i_Length = strlen(ca_SignInfo);
			
			while( i_Length > 0 )
			{
				if( ca_SignInfo[i_Length-1] != c_Previous )
				{
					i_Count++;
					c_Previous = ca_SignInfo[i_Length-1];
				}
				
				i_Length--;
			}
			
			printf( "\nCase #%d: %d\n", iIndex+1, i_Count );
			fprintf( file_output, "Case #%d: %d\n", iIndex+1, i_Count );
			
			//fprintf( file_output, "%s", ca_SignInfo );
			//printf( "\nSample:%s", ca_SignInfo );
			//i_Length = strlen(ca_SignInfo);
			//printf("\nLength: %d", i_Length);
		}
	}
	printf("\n");
} 