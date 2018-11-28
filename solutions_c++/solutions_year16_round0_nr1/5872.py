// ConsoleApplication5.cpp : Defines the entry point for the console application.
#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;


int main() {
	int T = 0;
	long int N = 0;
	vector <int> Numbers;
	ifstream infile;
	ofstream outfile;
	string line;

	infile.open("D:/GoogleCodeJam/CountingSheeplarge.in");
	outfile.open("D:/GoogleCodeJam/CountingSheeplarge.txt");


	if (infile.is_open())
	{
		bool first = true;
		while (getline(infile, line))
		{
			int intVal = atoi(line.c_str());
			if (first == true) {
				T = intVal;
				first = false;
			}
			else  {
				Numbers.push_back(intVal);
			}
			
		}
		infile.close();
	}

	else cout << "Unable to open file";
	for (int j = 0; j < Numbers.size(); j++) {
		N = 0;
		N = Numbers[j];

		if (N == 0) {
			outfile << "Case #" << j +1 << ": INSOMNIA" << endl;
			continue;
		}

		int A[10] = { 0 };
		int count = 0;

		int k = 2;
		int num = N;
		while (true) {
			int val = num;				 
			while (num > 0) {
				if (A[num % 10] == 0){
					A[num % 10] = 1;
					count++;
				}
				num = num / 10;
			}

			if (count == 10) {
				outfile << "Case #" << j+1 << ": " << val << endl;
				break;
			}
			num = k * N;
			k++;
		}

	}
	infile.close();
	outfile.close();
	_getch();
}