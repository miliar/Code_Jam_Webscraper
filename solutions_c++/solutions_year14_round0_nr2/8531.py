#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits.h>
#include <vector>
#include <iomanip>

using namespace std;

ifstream input;

double best_time;

void BestTime(double t_time, double C, double F, double X, double P) {

	double c_time = t_time + (C / P);
	double temp_time = c_time + (X / (P + F));

	if (temp_time < best_time) {
		best_time = temp_time;
		BestTime(c_time, C, F, X, P+F);
	}
}

int main () {

	input.open("input.txt");
	FILE* fp = fopen( "output.txt", "w" );

	int lenght = 0;
	input>>lenght;

	// Analizza i vari casi
	for (int i = 0; i < lenght; i++) {

		double C,F,X;

		input>>C;
		input>>F;
		input>>X;

		best_time = X / 2;

		BestTime(0, C, F, X, 2);

		fprintf(fp, "Case #%d: %1.7f\n", i+1, best_time);
		cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<best_time<<endl;
	}

	fclose(fp);
}

