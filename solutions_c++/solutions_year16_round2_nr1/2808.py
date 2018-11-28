#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

void printMap(unordered_map<char, int>& letters) {
	cout << "letters:" << endl;
	  for ( auto& x: letters )
		std::cout << x.first << ": " << x.second << std::endl;
	cout << "=====END===========" << endl;
}

void decrement(unordered_map<char, int>& letters, char c) {
	letters[c] = letters[c] - 1;
//	cout << c << " " << letters[c] << endl;
	if (letters[c] == 0) {
		letters.erase(c);
	} else if (letters[c] < 0) {
//		cout << c <<  " " << letters[c] << endl;
	}
//	printMap(letters);
//	cin.get();
}


string solveProblem(string line) {
	unordered_map<char, int> letters;
	for (int i = 0; i < line.length(); ++i) {
		//letters[line[i]]
		if (letters.find(line[i]) == letters.end()) {
			letters[line[i]] = 1;
		} else {
			letters[line[i]] = letters[line[i]] + 1;
		}
	}
	vector<int> answers;
	while (letters.find('Z') != letters.end()) {
		answers.push_back(0);
		decrement(letters, 'Z');
		decrement(letters, 'E');
		decrement(letters, 'R');
		decrement(letters, 'O');
	}
	while (letters.find('W') != letters.end()) {
		answers.push_back(2);
		decrement(letters, 'T');
		decrement(letters, 'W');
		decrement(letters, 'O');
	}

	while (letters.find('X') != letters.end()) {
		answers.push_back(6);
		decrement(letters, 'S');
		decrement(letters, 'I');
		decrement(letters, 'X');
	}

	while (letters.find('G') != letters.end()) {
		answers.push_back(8);
		decrement(letters, 'E');
		decrement(letters, 'I');
		decrement(letters, 'G');
		decrement(letters, 'H');
		decrement(letters, 'T');
	}
	while (letters.find('U') != letters.end()) {
		answers.push_back(4);
		decrement(letters, 'F');
		decrement(letters, 'O');
		decrement(letters, 'U');
		decrement(letters, 'R');
	}

	while (letters.find('T') != letters.end()) {
		answers.push_back(3);
		decrement(letters, 'T');
		decrement(letters, 'H');
		decrement(letters, 'R');
		decrement(letters, 'E');
		decrement(letters, 'E');
	}

	while (letters.find('S') != letters.end()) {
		answers.push_back(7);
		decrement(letters, 'S');
		decrement(letters, 'E');
		decrement(letters, 'V');
		decrement(letters, 'E');
		decrement(letters, 'N');
	}

	while (letters.find('V') != letters.end()) {
		answers.push_back(5);
		decrement(letters, 'F');
		decrement(letters, 'I');
		decrement(letters, 'V');
		decrement(letters, 'E');
	}

	while (letters.find('I') != letters.end()) {
		answers.push_back(9);
		decrement(letters, 'N');
		decrement(letters, 'I');
		decrement(letters, 'N');
		decrement(letters, 'E');
	}

	while (letters.find('O') != letters.end()) {
		answers.push_back(1);
		decrement(letters, 'O');
		decrement(letters, 'N');
		decrement(letters, 'E');
	}
	sort(answers.begin(), answers.end());
	ostringstream oss;
	for (int i = 0 ; i < answers.size(); ++i) {
		oss << answers[i];
	}
	return oss.str();
	//return to_string(temp);
}


int main(int argc, char* argv[])
{
	std::ifstream infile(argv[1]);
	string line;
	std::getline(infile, line);
	int num = stoi(line);
	for (int i = 1; i <= num; ++i) {
		std::getline(infile, line);
		cout << "Case #" << i << ": " << solveProblem(line) << endl;
	}
		
		
	return 0;


}