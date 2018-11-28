#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int trigger,trigger2,trigger3,trigger4;
	int **lawn;
	FILE *input,*output;
	input = fopen("B-small-attempt0.in", "r");
	output= fopen("Output.txt", "w");
	int tcase,length1,length2,num;
	char *str,*str2;
	fscanf(input,"%d", &tcase);
	for ( int i =0 ; i < tcase ; i++ ) 
	{
		trigger = 0;
		trigger2= 0;
		trigger3= 0;
		trigger4= 0;
		fscanf(input,"%d", &length1);
		fscanf(input,"%d", &length2);
		lawn = new int *[length1];
		for ( int j = 0; j < length1; j++)
			lawn[j] = new int [length2];
		for ( int j = 0; j < length1; j++)
		{
			for ( int k = 0; k < length2 ; k++ )
			{
				fscanf(input, "%d", &lawn[j][k]);
			}
		}
		
		for ( int j = 0 ; j < length1; j++)
		{
			for ( int k = 0 ; k <length2; k++ )
			{
				if ( lawn[j][k] == 1 )
				{
					for ( int x = 0; x < length2; x++)
					{
						if ( lawn[j][x] == 1 ) trigger++;
					}
					if ( trigger != length2 ) trigger2 = 1;
					trigger = 0;

					for ( int x = 0; x < length1; x++)
					{
						if ( lawn[x][k] == 1 ) trigger++;
					}
					if ( trigger != length1 ) trigger4 = 1;
					trigger = 0;
					if ( trigger2 == 1 && trigger4 == 1 )
					{	
						trigger3 = 1;
					}
					trigger2 =0;
					trigger4 =0;
				}
			}
		}
		if ( trigger3 == 0 ) fprintf(output, "Case #%d: YES\n", i+1);
		if ( trigger3 == 1 ) fprintf(output, "Case #%d: NO\n", i+1);
	}
	fclose(input);
	fclose(output);
	return 0;
}