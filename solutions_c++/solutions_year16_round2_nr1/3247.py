#include <iostream>
#include <fstream>
#include <String>
#include <vector>
#include <algorithm>

using namespace std;

string input; //Bullshit style :/ Hate competitive programming }:)

vector<int> output;

int findW() { //Procedure to find all 2

	int i = 0; //iPointer

	while ((i = input.find("W")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("T");
		input.erase(input.begin() + i);
		i = input.find("O");
		input.erase(input.begin() + i);
		output.push_back(2);
	}

	return 0;
}

int findU() { //All 4

	int i = 0;

	while ((i = input.find("U")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("F");
		input.erase(input.begin() + i);
		i = input.find("O");
		input.erase(input.begin() + i);
		i = input.find("R");
		input.erase(input.begin() + i);
		output.push_back(4);
	}

	return 0;
}

int findG() { //All 8

	int i = 0;

	while ((i = input.find("G")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		i = input.find("I");
		input.erase(input.begin() + i);
		i = input.find("H");
		input.erase(input.begin() + i);
		i = input.find("T");
		input.erase(input.begin() + i);
		output.push_back(8);
	}

	return 0;
}

int findZ() { //Guess what? 0!

	int i = 0;

	while ((i = input.find("Z")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		i = input.find("R");
		input.erase(input.begin() + i);
		i = input.find("O");
		input.erase(input.begin() + i);
		output.push_back(0);
	}

	return 0;
}

int findF() { //5

	int i = 0;

	while ((i = input.find("F")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("I");
		input.erase(input.begin() + i);
		i = input.find("V");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		output.push_back(5);
	}

	return 0;
}

int findH() { //3

	int i = 0;

	while ((i = input.find("H")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("T");
		input.erase(input.begin() + i);
		i = input.find("R");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		output.push_back(3);
	}

	return 0;
}

int findV() { //7

	int i = 0;

	while ((i = input.find("V")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("S");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		i = input.find("N");
		input.erase(input.begin() + i);
		output.push_back(7);
	}

	return 0;
}

int findS() { //6

	int i = 0;

	while ((i = input.find("S")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("I");
		input.erase(input.begin() + i);
		i = input.find("X");
		input.erase(input.begin() + i);
		output.push_back(6);
	}

	return 0;
}

int findO() { //1

	int i = 0;

	while ((i = input.find("O")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("N");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		output.push_back(1);
	}

	return 0;
}


int findN() { //9

	int i = 0;

	while ((i = input.find("N")) > -1) {
		input.erase(input.begin() + i);
		i = input.find("I");
		input.erase(input.begin() + i);
		i = input.find("N");
		input.erase(input.begin() + i);
		i = input.find("E");
		input.erase(input.begin() + i);
		output.push_back(9);
	}

	return 0;
}

int main() {

	fstream infile; 
	infile.open("A-large.in", ios_base::in | ios_base::app);
	fstream outfile;
	outfile.open("output.txt", ios_base::out | ios_base::app);

	int n;

	infile >> n;

	for (int i = 0; i < n; i++) {

		infile >> input;

		findW();
		findU();
		findG();
		findZ();
		findF();
		findH();
		findV();
		findS();
		findO();
		findN();

		sort(output.begin(), output.end());
		
		outfile << "Case #" << i + 1 << ": ";

		for (int i = 0; i < output.size(); i++) {
			outfile << output.at(i);
		}

		outfile << endl;

		output.clear();
	}

	return 0;
}