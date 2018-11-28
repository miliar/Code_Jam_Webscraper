#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int trigger,count;
	FILE *input,*output;
	input = fopen("C-small-attempt0.in", "r");
	output= fopen("Output.txt", "w");
	int tcase,lower,upper,num;
	char *str,*str2;
	fscanf(input,"%d", &tcase);
	for ( int i =0 ; i < tcase ; i++ ) 
	{
		count = 0;
		fscanf(input,"%d", &lower);
		fscanf(input,"%d", &upper);
		num = lower;
		for ( int j = lower; j <= upper; j++ )
		{
			if ( j < 10 )
			{
				for ( int k = 0; k <= j ; k++ )
				{
					if ((k*k) == j )
					{
						count++;
					}
				}
			}
			else
			{
				if ( j > 1000 )
				{
					str = new char[4];
					itoa (j,str,10);
					if ( str[0] == str[3] && str[2] == str[1] )
					{
						for ( int k = 0; k < j ; k++ )
						{
							if ((k*k) == j )
							{
								count++;
							}
						}
					}

				}
				else if ( j > 100 )
				{
					str = new char[3];
					itoa (j,str,10);
					if ( str[0] == str[2] )
					{
						for ( int k = 0; k < j ; k++ )
						{
							if ((k*k) == j )
							{
								str2 = new char[2];
								itoa(k,str2,10);
								if ( str2[0] == str2[1] )
								{
									count++;
								}
							}
						}
					}
				}
				else 
				{
					str = new char [2];
					itoa (j,str,10);
					if ( str[0] == str[1])
					{
						for ( int k = 0; k < j ; k++ )
						{
							if ((k*k) == j )
							{
								count++;
							}
						}
					}
				}
			}
		}
		fprintf(output,"Case #%d: %d\n", i+1, count);
	}
	fclose(input);
	fclose(output);
	return 0;
}