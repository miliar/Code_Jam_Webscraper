#include <cstdio>
#include <iostream>
#include <string.h>
#include <assert.h>
#define NBSTRINGS 101
#define MAXLENGTH 101


struct _test 
{
	char chaines[NBSTRINGS][MAXLENGTH];
	char contract[NBSTRINGS][MAXLENGTH];
	int runlength[NBSTRINGS][MAXLENGTH];
	int nb;
};
typedef struct _test * test;


void contract_one(char * st1, char * st2, int * runs)
{
	int i=0, j=0;
	char current;
	int runLength ;
	while(st1[i] != '\0')
	{
		current = st1[i];
		runLength = 0;
		st2[j]= current;
		while(current == st1[i])
		{
			runLength ++;
			i++;
		}
		runs[j]= runLength;
		j++;
	}
	st2[j] = '\0';
}

void contract_all(test t)
{
	int nb = t->nb ;
	for(int i =0 ; i< nb; i ++)
	{
		contract_one(t->chaines[i], t->contract[i], t->runlength[i] );
	}
}

bool possible(test t)
{
	int nb = t->nb, length;
	int length0 = strlen(t->contract[0]);
	for(int i =0 ; i< nb; i ++)
	{
		length = strlen(t->contract[i]);
		//assert(length  == length0);
		if(strcmp(t->contract[0], t-> contract[i]) !=0)
			return false;
	}
	return true;
}

void parse_number_of_tests(FILE * file, int * number)
{
	fscanf(file, "%d", number);
}


void parse_one_test(FILE * file, test t)
{

	fscanf(file, "%d", &t->nb);	
	for(int i = 0; i< t->nb; i++)
	{
		fscanf(file, "%s\n", &t->chaines[i]);
	}
}

int compar(const int* a , const int* b)
{
	if(*a<*b)
		return -1;
	if(*a==*b)
		return 0;
	else 
		return 1;
}

int mediane_colonne(test t, int col)
{
	int tab [101];
	for(int i=0; i<101; i++)
	{
		tab[i] = t->runlength[i][col];
	}
	qsort(tab, t->nb, sizeof(int), (int (*) (const void*, const void*))compar);

	return tab[t->nb/2];
}

#define ABS(a) (((a)>=0)?(a):-(a))

int solve(test t)
{
	contract_all(t);
	int res = 0;

	if (!possible(t))
		return -1;

	int len = strlen(t->contract[0]);
	for(int j=0; j<len;j++)
	{
		int mediane = mediane_colonne(t, j);
		for(int i=0; i<t->nb; i++)		
		{
		
			res += ABS(t->runlength[i][j]- mediane);
		}
	}

	return res;
}


void solve_one_test(FILE * inputFile)
{
	test currentTest = (test) malloc(sizeof(*currentTest));
	parse_one_test(inputFile, currentTest);

	int result = solve(currentTest);
	if (result == -1)
	{
		std::cout << "Fegla won" << std::endl;
	}
	else
	{
		std::cout << result << std::endl;
	}

}

void solve_input_file()
{
	int numberOfTests;
	FILE * inputFile= fopen ("inputL.in", "r");
	parse_number_of_tests(inputFile, &numberOfTests);

	for(int i =0; i< numberOfTests; i++)
	{
		std::cout << "Case #" << i+1 << ": ";
		solve_one_test(inputFile);
	}
}

int main(int argc, char * argv[])
{
	solve_input_file();
	//system("PAUSE");
	return EXIT_SUCCESS;
}