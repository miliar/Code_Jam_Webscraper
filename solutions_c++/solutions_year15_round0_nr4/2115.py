#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

#define RICHARD 0
#define GABRIEL 1

int solve(int X, int R, int C){
	int grid = R * C;
	if (grid % X != 0 || X >= 7){
		return RICHARD;
	}
	
	for (int i = 1; i <= X; i++){
		int d1 = i, d2 = (X + 1 - i), area = d1 * d2;
		if (area > grid){
			return RICHARD;
		}
		if ((R < d1 && C < d2) ||
			(R < d2 && C < d1)){
			return RICHARD;
		}
	}
	
	if (X == 4 && (R <= 2 || C <= 2)){
		return RICHARD;
	}
	
	return GABRIEL;
}


int main(){
	ifstream input("D_small.in");
	ofstream output("output.txt");
	int numberOfCases, i = 0, X, R, C;
	
	input >> numberOfCases;
	while (input >> X >> R >> C){
		int solution = solve(X, R, C);
		output << "Case #" << ++i << ": " << (solution == RICHARD ? "RICHARD" : "GABRIEL") << endl;
	}
}