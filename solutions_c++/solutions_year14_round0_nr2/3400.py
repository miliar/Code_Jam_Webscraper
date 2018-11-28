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


int main(void) {
	std::ifstream inputFile;
	int test_cases =0;
	double C=0;
	double F=0;
	double X=0;

	std::string line;


	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
    	double cokies_per_second=2;
    	double total_cockies=0;
    	double total_seconds=0;

    	inputFile >> C;
    	inputFile >> F;
    	inputFile >> X;


		for(total_cockies=0;total_cockies<X;) {
			double lineal = X/cokies_per_second;
			double next_farm = C/cokies_per_second;
			if(lineal > (next_farm + ((X)/(cokies_per_second+F))  )) {
				cokies_per_second = cokies_per_second + F;
				total_seconds = total_seconds + next_farm;
			} else {
				total_seconds = total_seconds + lineal;
				total_cockies = X;
			}
		}


    	printf("Case #%d: %.7f\n",cases_executed, total_seconds);
	}

    inputFile.close();
    return 1;
}

