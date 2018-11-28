#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int numberOfZeros(string smax, string slevels);

int main(){
	int t;
	string smax;
	string slevels;
	vector<string> vs;

	ifstream fin;
	fin.open("Input.txt");

	// read in number of lines in file
	fin >> t;

	cout << "Number of test cases: " << t << endl;
	// Print results to file
	ofstream fout;
	fout.open("Output.txt");

	for (int i = 0; i < t; i++){
		fin >> smax;
		fin >> slevels;
		//cout << "Max shyness: " << smax << " Shyness for each: " << slevels << endl;
		cout << "Case #" << i+1 << ": " << numberOfZeros(smax, slevels) << endl;
		fout << "Case #" << i + 1 << ": " << numberOfZeros(smax, slevels) << endl;
		
		
	}
	fout.close();
	cout << "---END OF FILE---" << endl << endl;
	cout << "Output has been generated to file Output.txt. Operation complete." << endl;
	cout << endl << endl;
	system("PAUSE");
}

int numberOfZeros(string smax, string slevels){
	int n = stoi(smax);
	int clappers = 0;
	int counter = 0;
	for (int i = 0; i < n + 1 ; i++){
		if (clappers + counter < i)
			counter++;
		int x = slevels.at(i) - '0';
		clappers += x;
	}
	return counter;
}

