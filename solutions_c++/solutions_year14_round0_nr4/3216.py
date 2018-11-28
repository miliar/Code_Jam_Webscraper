#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stdio.h"
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <list>
#include <algorithm>


int compare (const void * a, const void * b)
{
    if(*(const double*)a < *(const double*)b)
        return -1;
    return *(const double*)a > *(const double*)b;}


int main(void) {
	std::ifstream inputFile;
	int test_cases =0;
	std::string line;
	std::string result ="";
	double naomi[1000];
	double ken[1000];

	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
    	int total_blocks = 0;
    	int result1 = 0;
    	int result2 = 0;

    	inputFile >> total_blocks;
    	for(int i=0;i<total_blocks;i++)
        	inputFile >> naomi[i];
    	for(int i=0;i<total_blocks;i++)
        	inputFile >> ken[i];

        qsort(naomi, total_blocks, sizeof(double), compare);
        qsort(ken, total_blocks, sizeof(double), compare);


        for(int i=0,aux1 = 0;i<total_blocks;i++) {
        	if(naomi[i] > ken[aux1]) {
        		result1++;
        		aux1++;
        	}
        }

        for(int i=1, aux = 1;i<=total_blocks;i++) {
        	if(naomi[total_blocks - i] > ken[total_blocks - aux]) {
        		result2++ ;
        	} else
        		aux++;
        }

		std::cout << "Case #" << cases_executed << ": " << result1  << " " << result2 << std::endl;
	}

    inputFile.close();
    return 1;
}

