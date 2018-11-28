#include <stdio.h>
using namespace std;

const char* fname = "file.in";
const char* fnameo = "fileo.in";
int giveOutput(int* a, int* b, int A, int B);

int main()
{
FILE *file, *fileo;
file = fopen(fname, "r+");
fileo = fopen(fnameo, "w+");
int array1[16], array2[16];
int a, b, guess1, guess2, i = 0;
fscanf(file, "%d\n", &a);
printf("Number of test cases : %d\n", a);

while(!feof(file) && i < a)
{
fscanf(file, "%d\n", &guess1);
fscanf(file, "%d %d %d %d\n", &array1[0], &array1[1], &array1[2], &array1[3]);
fscanf(file, "%d %d %d %d\n", &array1[4], &array1[5], &array1[6], &array1[7]);
fscanf(file, "%d %d %d %d\n", &array1[8], &array1[9], &array1[10], &array1[11]);
fscanf(file, "%d %d %d %d\n", &array1[12], &array1[13], &array1[14], &array1[15]);

fscanf(file, "%d\n", &guess2);
fscanf(file, "%d %d %d %d\n", &array2[0], &array2[1], &array2[2], &array2[3]);
fscanf(file, "%d %d %d %d\n", &array2[4], &array2[5], &array2[6], &array2[7]);
fscanf(file, "%d %d %d %d\n", &array2[8], &array2[9], &array2[10], &array2[11]);
fscanf(file, "%d %d %d %d\n", &array2[12], &array2[13], &array2[14], &array2[15]);

b = giveOutput(array1, array2, guess1, guess2);
if(b == -99)
	{
		fprintf(fileo, "Case #%d: Volunteer Cheated!\n", i + 1);
		printf("Case #%d: Volunteer Cheated!\n", i + 1);
	}
else if(b == 0)
	{
		fprintf(fileo, "Case #%d: Bad Magician!\n", i + 1);
		printf("Case #%d: Bad Magician!\n", i + 1);
	}
else
	{
		fprintf(fileo, "Case #%d: %d\n", i + 1, b);
		printf("Case #%d: %d\n", i + 1, b);
	}

i++;
}

fclose(file);
fclose(fileo);
return 0;
}

int giveOutput(int* a, int* b, int A, int B)
{
	int row1 = A - 1;
	int row2 = B - 1;
	int count = 0;
	int the_number = -99;
	
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{	
			if(a[4*row1 + i] == b[4*row2 + j])
			{
				if(count < 1)
					{
					count++;
					the_number = a[4*row1 + i];
					}
				else
					{
					the_number = 0;
					break;
					}
			}
		}
	}
	
	return the_number;
}
