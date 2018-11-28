//Farhan Javed - NUCES - Pakistan

#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
	ifstream inFile;
	inFile.open("B-large.in");
	ofstream outputFile;
	outputFile.open("answers.txt");
	outputFile << fixed << showpoint << setprecision(7);
	double C, F, X, cookies_per_second = 2.0, test = 0.0, t_seconds = 0.0,
			prev_result = 0.0, result = 0.0, lowest;
	int x, y = 1;
	inFile >> x;
	while (x > 0) {
		cookies_per_second = 2.0;
		t_seconds = 0.0;
		prev_result = 0.0;
		result = 0.0;
		inFile >> C;
		inFile >> F;
		inFile >> X;
		result = X / cookies_per_second;
		lowest = result;
		while (1) {
			prev_result = result;
			t_seconds += C / cookies_per_second;
			cookies_per_second += F;
			test = X / cookies_per_second;
			result = test + t_seconds;
			if (result < prev_result) {
				lowest = result;
			}
			else if (result > prev_result){
				result = lowest;
				break;
			}
		}
		outputFile << "Case #" << y << ": " << result << endl;
		x--;
		y++;
	}
	outputFile.close();
	return 0;
}
