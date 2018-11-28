#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int CountFriends(string input) {
	int shy_level_max = atoi(&input.at(0));
	//input.at(2);
	int total = 0;
	int friends = 0;
	for(int i=0; i<=shy_level_max; i++) {
		if(total < i) {
			friends += (i - total);
			total += (i - total);
		}
		const char a = input.at(i+2);
		total += atoi(&a);
	}
	return friends;
}

int main (int argc, char* argv[]) {
	if(argc != 2) {
		cout << "File not set!" << endl;
		return 1;
	}
	cout << argv[0] << endl;
	cout << argv[1] << endl;
	list<string> inputvalues;
	string line;
	ifstream inputfile;
	inputfile.open((const char*)argv[1],ios::in);
	if (inputfile.is_open()) {
		while ( getline(inputfile,line) ) {
			inputvalues.push_back(line);
			line.clear();
		}
		inputfile.close();
	}
	else {
		cout << "Unable to open file";
		return 2;
	}
	int testcases = atoi(inputvalues.front().c_str());
	inputvalues.pop_front();
	int* friends = new int[testcases];
	for(int i=0; i<testcases; i++)
		friends[i] = 0;
	while(inputvalues.size() > 0) {
		friends[inputvalues.size() - 1] = CountFriends(inputvalues.back());
		inputvalues.pop_back();
	}
	ofstream outputfile ("output.txt");
	if (outputfile.is_open()) {
		for(int i=0; i< testcases; i++)
			outputfile << "Case #" << i +1 << ": " << friends[i] << endl;
		outputfile.close();
	} else 
		cout << "Unable to open file";
	delete[] friends;
	return 0;
}