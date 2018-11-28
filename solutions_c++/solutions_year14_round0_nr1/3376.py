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

std::ifstream inputFile;


int get_entire_row(int entire[], int row_number){
	for(int j=0;j<4;j++) {
		if(j+1 == row_number) {
			for (int z=0;z<4;z++){
				inputFile >> entire[z];
			}
		} else {
			for (int z=0;z<4;z++){
				int aux=0;
				inputFile >> aux;
			}
		}
	}
return 0;
}

int main(void) {
	int test_cases =0;
	int row_number = 0;
	int entire_row_1[4];
	int entire_row_2[4];
	std::string line;
	int result = 0;


	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
			inputFile >> row_number ;
			get_entire_row(entire_row_1,row_number);

			inputFile >> row_number ;
			get_entire_row(entire_row_2,row_number);

			result = 0;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++){
					if(entire_row_1[i]==entire_row_2[j])
						if (result == 0)
							result = entire_row_1[i];
						else {
							result = -1;
							break;
						}
				}
		if (result == 0)
			std::cout << "Case #" << cases_executed << ": " << "Volunteer cheated!"  << std::endl;
		else if (result > 0 )
			std::cout << "Case #" << cases_executed << ": " << result  << std::endl;
		else
			std::cout << "Case #" << cases_executed << ": " << "Bad magician!"  << std::endl;
	}

    inputFile.close();
    return 1;
}

