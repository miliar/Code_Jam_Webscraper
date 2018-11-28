#include <stdint.h>
#include <stdio.h>
#include <fstream>


unsigned int iu_NumOfBitsToUse, iu_NumOfCoinsToMake, iu_CoinsMade, iu_DivisorFound, iu_IsAPrimeNum = 0;
signed int i_Cases;
unsigned long long llu_CoinUnderEvaluation, llu_CoinBaseChanged, llu_Divisor[11];

unsigned long long fn_ConvertCoin( long long llu_CoinToConvert,  unsigned int iu_base );
unsigned long long fn_power( unsigned int iu_num, unsigned int iu_pow );

int main( void )
{
	FILE *file_input, *file_output;
	
	file_input = fopen( "inputfile.in", "r" );
	file_output = fopen( "output_small.txt", "w" );
	if( (file_input != NULL) && (file_output != NULL) )
	{
		fscanf( file_input, "%d", &i_Cases );
		
		if( i_Cases == 0 )
		{
			printf( "\nError in number of cases\n" );
		}
		for( int iIndex = 0; iIndex < i_Cases; iIndex++ )
		{
			fscanf( file_input, "%u", &iu_NumOfBitsToUse );
			fscanf( file_input, "%u", &iu_NumOfCoinsToMake );
			
			
			printf( "\nNumber of bits to use = %u", iu_NumOfBitsToUse );
			printf( "\nNumber of coins to make = %u", iu_NumOfCoinsToMake );
			
			// Initialize the data
			iu_CoinsMade = 0;
			llu_CoinUnderEvaluation = 0;
			
			// Create coin
			if( iu_NumOfBitsToUse == 16 )
			{
				llu_CoinUnderEvaluation = 0x8001;
			}
			else if( iu_NumOfBitsToUse == 32 )
			{
				llu_CoinUnderEvaluation = 0x80000001;
			}
			else if( iu_NumOfBitsToUse == 6 )
			{
				llu_CoinUnderEvaluation = 0x21;
			}
			else
			{
				printf("\nProblem: The bits to use is not read correctly");
			}
			
			printf( "\nCase #%d:\n", iIndex+1 );
			fprintf( file_output, "Case #%d:", iIndex+1 );
			
			while( (iu_CoinsMade < iu_NumOfCoinsToMake) && (llu_CoinUnderEvaluation < 0x100000000) )
			{
				printf( "\nCoin under evaluation:%llu", llu_CoinUnderEvaluation );
				printf( "\nCoin number: %u", iu_CoinsMade );
				iu_IsAPrimeNum = 0;
				for( int i = 2; i <= 10; i++ )  /* Counting the base */
				{
					// Convert base
					//printf("\nAbout to start conversion\n");
					llu_CoinBaseChanged = fn_ConvertCoin( llu_CoinUnderEvaluation, i );
					//fflush(stdin);
					//fflush(stdout);
					//printf("\nDone with conversion\n");
					
					printf("\nConverted number:%llu ,Base: %d", llu_CoinBaseChanged, i );
					printf("\n");
					// Check for prime
					iu_DivisorFound = 0;
					for( unsigned long long llu_j = 2; llu_j <= ( (llu_CoinBaseChanged / 2) + 1 ); llu_j++ )
					{
						unsigned int iu_Remainder = 0;
						
						//printf("\nInside the prime calculation. Index %llu", llu_j);
						
						iu_Remainder = llu_CoinBaseChanged % llu_j;
						
						if( iu_Remainder == 0 )
						{
							// Got a divisor, so number is not prime and may be a jam coin
							iu_DivisorFound = 1;
							llu_Divisor[i] = llu_j;
							printf( "\nDivisor - %llu", llu_Divisor[i] );
							break;
						}
						
						if( (llu_j * llu_j) > llu_CoinBaseChanged )
						{
							break;
						}
						
					}
					if( iu_DivisorFound == 0 )
					{
						// This is a prime number. So, is not a jam coin
						printf("\nThis is a prime number");
						iu_IsAPrimeNum = 1;
						break;
					}
					//printf("Found the divisor, Loop number %d\n", i);
				}
				printf("\n");
				//printf("Came out of loop\n");
				if( iu_IsAPrimeNum == 0 )
				{
					iu_CoinsMade++;
				
					printf( "%llu ", llu_CoinUnderEvaluation );
					//fprintf( file_output, "%llu ", llu_CoinUnderEvaluation );
					
					unsigned long long llu_ConvToBinary = llu_CoinUnderEvaluation;
					unsigned long long llu_BinaryConverted = 0;
					unsigned int iu_Count = 0;
					
					//fprintf( file_output, "\n" );
					while( llu_ConvToBinary ) 
					{
						if ( llu_ConvToBinary & 1 )
						{
							llu_BinaryConverted = llu_BinaryConverted + fn_power( 10, iu_Count);
							//printf("1");
							//fprintf( file_output, "1" );
						}
						else
						{
							//printf("0");
							//fprintf( file_output, "0" );
						}
						iu_Count++;
						llu_ConvToBinary >>= 1;
					}
					//fprintf( file_output, "\n%llu ", llu_CoinUnderEvaluation );
					fprintf( file_output, "\n%llu ", llu_BinaryConverted );
					printf( "\n%llu ", llu_BinaryConverted );
					//printf(" ");
					//fprintf( file_output, " " );
					
					for( int k = 2; k <= 10; k++ )  /* Counting the base */
					{
						printf( "%llu ", llu_Divisor[k] );
						fprintf( file_output, "%llu ", llu_Divisor[k] );
					}
					
				}
				// Move to the next coin
				llu_CoinUnderEvaluation = llu_CoinUnderEvaluation + 0x02;
			}
			
			
		}
	}
	else
	{
		printf("\nError opening one of the files");
	}
	printf("\n");
	
	
	//printf( "\nTest covnertion - %llu %llu %llu\n", fn_ConvertCoin(100011, 2), fn_ConvertCoin(111111, 2), fn_ConvertCoin(111001, 2) );
}


unsigned long long fn_ConvertCoin( long long llu_CoinToConvert,  unsigned int iu_base )
{
	unsigned long long llu_ConvertedCoin = 0;
	unsigned int iu_BitValue = 0, iu_PowerPos = 0;
	
	while( llu_CoinToConvert > 0 )
	{
		iu_BitValue = llu_CoinToConvert % 2;
		llu_CoinToConvert = llu_CoinToConvert / 2;
		
		llu_ConvertedCoin = llu_ConvertedCoin + ( iu_BitValue * fn_power( iu_base, iu_PowerPos ) ); 
		iu_PowerPos++;
	}
	//printf("\nConversion done inside the local function");
	return llu_ConvertedCoin;
}

unsigned long long fn_power( unsigned int iu_num, unsigned int iu_pow )
{
	unsigned long long llu_value = 1;
	
	while( iu_pow > 0 )
	{
		llu_value = iu_num * llu_value;
		iu_pow--;
	}
	return llu_value;
}

