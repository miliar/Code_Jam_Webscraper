#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdlib>
using namespace std;

int main() {
	ifstream in;
	in.open("B-large.txt");
	double number;
	vector<double> list;
	int casenumber;
	string s;

	ofstream answerFile;
	answerFile.open("answer2b.txt");

	getline(in, s);
	stringstream line(s);
	string eachInt;	
	line >> eachInt;
	stringstream convert(eachInt);
	convert >> casenumber;

	while (getline(in, s)) {
		stringstream line(s);
		string eachDouble;
		while (line >> eachDouble) {
			number = atof(eachDouble.c_str());
			list.push_back(number);
		}
	}

	double x;
	double y;
	double acc;

	for (int i = 1; i <= casenumber; i++) {
		x = list[2]/2;
		y = list[0]/2 + list[2]/(2+list[1]);
		acc = 2;
		while (x > y) {
			x = y;
			y = y + list[0]/(acc+list[1]) - list[2]/(acc+list[1]) + list[2]/(acc+2*list[1]);
			acc += list[1];
		}
		answerFile << "Case #" << i << ": " << setprecision(7) << fixed << x << "\r\n";
		list.erase(list.begin(), list.begin()+3);
	}
	in.close();
	answerFile.close();
	
	return 0;
}



