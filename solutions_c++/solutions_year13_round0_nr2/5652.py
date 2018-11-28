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

int test_cases =0;
std::string line;
std::string result ="";
char lawn[100][100];
int lx;
int ly;

bool bigger_x(int x, int y) {
	for(int i=0;i<ly;i++)
		if(lawn[x][i] > lawn[x][y])
			return true;
return false;
}

bool bigger_y(int x, int y) {
	for(int i=0;i<lx;i++)
		if(lawn[i][y] > lawn[x][y])
			return true;
	
return false;
}


std::string solve(){

	for(int i=0;i<lx;i++)
		for(int j=0;j<ly;j++) {
			if(bigger_x(i,j) && bigger_y(i,j))
				return "NO";
		}

	return "YES";
}

int main(void) {
	std::ifstream inputFile;
	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
    	inputFile >> lx;
    	inputFile >> ly;

    	for(int i=0;i<lx;i++)
    		for(int j=0;j<ly;j++)
				inputFile >> lawn[i][j];    		
/*
		std::cout << lx << " " << ly <<std::endl;
    	for(int i=0;i<lx;i++) {
    		for(int j=0;j<ly;j++)
				std::cout << lawn[i][j];    		
			std::cout << std::endl;
		}
*/
		
		result = solve();

		std::cout << "Case #" << cases_executed << ": " << result  << std::endl;
	}

    inputFile.close();
    return 1;
}
