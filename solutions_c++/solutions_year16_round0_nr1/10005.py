//============================================================================
// Name        : CountingSheep.cpp
// Author      : Mohammed
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include <assert.h>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <cmath>

int main() {
	// open input file
	FILE* inptr = fopen("A-large.in","r");
	assert(inptr != NULL);

	// open output file
	FILE* outptr = fopen("out.txt","w");
	assert (outptr != NULL);
	// reading data
	unsigned int T;
	unsigned int N[102];
	fscanf(inptr,"%d", &T);
	for(unsigned int i = 0; i < T; i++)
		fscanf(inptr,"%d", &N[i]);

	for(unsigned int i = 0; i < T; i++)
	{
		fprintf(outptr,"%s%d%s","Case #",i+1,": ");
		// if n = 0 will count forever
		if(N[i] == 0)
		{
			// print INSOMNIA
			fprintf(outptr,"%s", "INSOMNIA\n");
		}
		else
		{
			int dot_count = 0;
			char numbers [] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
			char number[100];
			int sweeped_number = N[i];
			// loop until find all numbers(assume max. number 2112 to find all numbers)
			for (int j = 2; j<= 2112; j++)
			{
				// each loop check number by converting it to string
				itoa(sweeped_number,number,10);
				// comparing number with the elements in the array
				for(int k = 0; k < strlen(number); k++)
				{
					for(int l = 0; l <= 9; l++)
					{   // if number is found convert the number to '.'
						if(number[k] == numbers[l])
						{
							numbers[l] = '.';
							break;
						}
					}
				}
				// check if all array is dotted
				for(int l = 0; l <= 9; l++)
				{
					if(numbers[l] != '.')
						break;
					else
						dot_count++;
				}
				// if all is dotted output the number(last number before fall asleep)
				if (dot_count == 10)
				{
					fprintf(outptr,"%s%s", number,"\n");
					break;
				}
				else
				{
					// if not multiply original number by 2,3
					sweeped_number = j*N[i];
					dot_count = 0;
				}
		    }
			// if loop finishes and the array is not all dotted print INSOMNIA
			dot_count = 0;
			for(int l = 0; l <= 9; l++)
			{
				if(numbers[l] != '.')
					break;
				else
					dot_count++;
			}
			// if all is dotted output the number(last number before fall asleep)
			if (dot_count != 10)
			{
				fprintf(outptr,"%s", "INSOMNIA\n");
			}
		}

	}
	return 0;
}
