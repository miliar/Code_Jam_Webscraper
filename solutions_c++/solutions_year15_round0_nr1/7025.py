#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

vector<string> split(string line, string delimit=" ") {
	vector<string> words;
	int pos = line.find(delimit);
	int start = 0;
	while (pos != -1) {
		words.push_back(line.substr(start, pos-start));
		start = pos+1;
		pos = line.substr(start,line.size()-start).find(delimit);
	}
	if(start == 0) {
		words.push_back(line);
	}
	else {
		if (pos == -1) {
			words.push_back(line.substr(start,line.size()-start));	
		}
	}
	return words;
}

int standingOvation(vector<string> numbers) {
	string aud = numbers[1];
	int present = 0;
	int needed = 0;
	int required = 0;
	for(int i = 0; i < aud.size(); i++) {
		if (present >= needed) {
			needed += 1;
		}
		else {
			required += (needed-present);
			present += (needed-present);
			needed += 1;
		}
		present += (aud[i]-'0');
	}
	return required; 
}

int main() {
	string line;
	fstream myfile;
	myfile.open("A-large.in");
	vector<int> visitors;
	int test = 0;
	if (myfile.is_open()) {
		while (getline(myfile,line)) {
			vector<string> words = split(line);
			if (words.size() > 1) {
				visitors.push_back(standingOvation(words));
			}
		}
		myfile.close();
		myfile.clear();
	}
	else {
		cout << "Can't open the file";
	}
	myfile.open("output.txt");
	if(myfile.is_open()) {
		for (int i = 0; i < visitors.size(); i++) {
			myfile << "Case #" << i+1 << ": " << visitors[i] << "\n";
		}
		myfile.close();
	}
	return 0;
}
