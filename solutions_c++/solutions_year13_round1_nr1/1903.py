#include <cstdlib>
//#include <cstring>
#include <cstdio>
//#include <iostream>
#include <list>
//#include <map>
#include <cmath>

//gmplib http://gmplib.org/ 
#include <gmp.h>

#define FILE_NAME_BASE "a"

//const double pi = 3.14159265359;

typedef struct
{
	unsigned int num;
	unsigned long long radius;
	unsigned long long paint;
	unsigned long long result;
} Case;

int main()
{
	//File input
	FILE* fin = fopen(FILE_NAME_BASE".in", "r");
	if (fin == NULL) { puts("Error: could not open input file!\n"); exit(EXIT_FAILURE); }
	
	//Load input
	unsigned int numOfCases;
	fscanf(fin, "%u", &numOfCases);
	
	std::list<Case> cases;
	
	for (int i=0; i < numOfCases; i++)
	{
		Case tmp;
		tmp.num = cases.size();
		fscanf(fin, "%llu", &(tmp.radius));
		fscanf(fin, "%llu", &(tmp.paint));
		tmp.result = 0;
		cases.push_back(tmp);
	}
	
	
	fclose(fin);
	
	//Caclulate
	for (std::list<Case>::iterator it = cases.begin(); it != cases.end(); ++it)
	{
		printf("%u\n", (*it).num);
		for (int offset = 0; ; offset += 2)
		{
			unsigned long long area = (pow((*it).radius+offset+1, 2) - pow((*it).radius+offset, 2));
			if (area > (*it).paint)
			{
				//printf("1");
				break;
			}
			else if (area == (*it).paint)
			{
				//printf("2");
				(*it).result++;
				break;
			}
			else
			{
				//printf("3");
				(*it).paint -= area;
				(*it).result++;
			}
		}
	}
	
	
	//File output
	FILE* fout = fopen(FILE_NAME_BASE".out", "w");
	if (fout == NULL) { puts("Error: could not open output file!\n"); exit(EXIT_FAILURE); }
	
	//Write output
	
	for (std::list<Case>::iterator it = cases.begin(); it != cases.end(); ++it)
	{
		fprintf(fout, "Case #%u: %llu\n", (*it).num+1, (*it).result);
	}
	
	fclose(fout);
	return EXIT_SUCCESS;
}