#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("result.txt");

	fout << fixed << setprecision(7);

	int times;
	int max_buy_times;

	fin >> times;

	for (int i = 0; i < times; i++){
		double C, F, X;
		fin >> C;
		fin >> F;
		fin >> X;

		double max_time = X / 2;
		

		max_buy_times = 2000;
		double* time = new double[50000];
		int time_num = 0;

		for (int j = 0; j < max_buy_times; j++){
			double this_time = 0;
			double income = 2;

			for (int k = 0; k < j; k++){
				this_time += C / income;
				income += F;
			}

			this_time += X / income;
			time[j] = this_time;
			time_num += 1;
			//cout << j << " " << time[j] << endl;
			//system("PAUSE");
		}

		double a = time[0];
		for (int j = 0; j < max_buy_times; j++){
			if (time[j] < a){
				a = time[j];
			}
		}
		fout << "Case #" << i + 1 << ": " << a << endl;
	}

	fin.close();
	fout.close();
	return 0;
}