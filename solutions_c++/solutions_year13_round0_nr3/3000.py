#include <string>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <limits.h>

typedef unsigned __int64 lint; 

#define F(i,b) for(lint i=0;i<(b);i++)
#define FIAN(i,a,n) for(lint i=a;i<n;i++)
#define FIANrev(i,a,n) for(lint i=a;i>n;i--)

using namespace std;

FILE * inputFile = fopen("D:\\Downloads\\Chrome\\C-small-attempt1.in", "r");
FILE * outputFile  = fopen("D:\\Downloads\\Chrome\\output.txt", "w");

int A, B;
int numbers[] = {1, 4, 9, 121, 484};
int count;

void oneStep()
{
	count = 5;

	fscanf(inputFile, "%d %d", &A, &B);

	F(i, 5)
		if (A > numbers[i])
			count--;
		else
			break;

	F(i, 5)
		if (B < numbers[4 - i])
			count--;
		else
			break;

	fprintf(outputFile, "%d", count);
	fprintf(outputFile, "\n");
}

int main()
{
	time_t timer = time(NULL);
	printf("%s\n", ctime(&timer));

	unsigned int T;
	fscanf(inputFile, "%d", &T);

	F(t,T){
		//TODO: solve here!
		fprintf(outputFile, "Case #%d: ", t+1);
		oneStep();
		timer = time(NULL);
		printf("step %d - %s\n", t, ctime(&timer));
	}

	fclose(inputFile);
	fclose(outputFile);

	timer = time(NULL);
	printf("%s\n", ctime(&timer));
	// qDebug("Time elapsed: %d ms", time1.elapsed());
	return 0;
}