
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm> 

using namespace std;

int main(int argc, char* argv[]) {


	vector<int> lines;


	//cout << "Case" << endl;

	ifstream file(argv[1]);
	ofstream myfile("example.txt");

	int numCases;
	int maxShyness;
	string line;
	

	file >> numCases;
	int numCase = 0;

	while (file >> maxShyness >> line) {

		numCase++;
		vector<int> values;
		for (int i = 0; i < line.size(); i++) {
			int num = line[i] - '0';
				values.push_back(num);
		}

		int sum = 0;
		int persons = 0;

		for (int i = 0; i < values.size(); i++) {
			int val = values.at(i);

			if (val != 0) {
				int diff = i - sum;
				persons += max(diff, 0);
				sum += persons;
				sum += val;
			}
			

		}

		myfile << "Case #" << numCase << ": " << persons << endl;
		cout << "Case #" << numCase << ": " << persons << endl;


	}


}