#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<cmath>
#include<string>
#include<climits>
#include<stack>
#include <iomanip>      // std::setprecision
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

double solve(double C, double F, double X, double G, double saved){
	if (saved >= X) return 0;
	if ((X - saved) / G <= (X - saved + C) / (F + G)) return (X - saved) / G;
	else if(saved>=C) return solve(C, F, X, G + F, saved - C);
	else if (saved + G>C) return 1.0 * ((C - saved)) / G + solve(C, F, X, G, C);
	else return 1+solve(C, F, X, G , saved + G);
}

int main(){
	int T;
	double C, F, X;
	fin >> T;
	for (int k = 0; k < T; k++){
		fin >> C >> F >> X;
		fout << "Case #" << k + 1 << ": " <<fixed<< std::setprecision(7) << solve(C, F, X, 2, 0) << endl;
	}

}