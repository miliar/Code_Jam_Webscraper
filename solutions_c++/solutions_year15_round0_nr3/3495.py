#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>

/*
 * HELPER FUNCTIONS PROTOTYPES
 */

std::pair<int, std::string> createPair(std::ifstream &infile);

std::string handleTestCase(std::pair<int, std::string> &pair);


/*
 * Tokenizes the passed in string using passed in delimeters.
 * The passed in vector is cleared and then tokens are added to it.
 */
void tokenize(std::vector<std::string> &buf, std::string s, const char *delimeters = " ");

// global state is BAD
std::map<std::string, char> calcCache;

char calcChar(std::string &s);

inline void addToCache(char c, std::string s) {
	if (calcCache.find(s) == calcCache.end()) {
		calcCache.insert(std::pair<std::string, char>(s, c));
	}
}

inline bool isInCache(std::string s) {
	return calcCache.find(s) != calcCache.end();
}

void warmUpCache(std::string &s);

/*
* MAIN FUNCTION
*/
int main(int argc, char *argv[]) {
	if (argc != 3) {
		std::cerr << "must include an input and output file!" << std::endl;
		return 1;
	}

	std::ifstream infile(argv[1]);
	std::ofstream outfile(argv[2]);
	
	if (!infile.is_open() || !outfile.is_open()) {
		std::cerr << "File I/O error!" << std::endl;
		return 2;
	}
	
	// get number of test cases
	std::string line;
	std::getline(infile, line);
	int testCases = atoi(line.c_str());

	std::vector<std::pair<int, std::string>> inputvector;

	for (int i = 0; i < testCases; ++i) {
		inputvector.push_back(createPair(infile));
	}

	for (int i = 0; i < inputvector.size(); ++i) {
		warmUpCache(inputvector[i].second);
	}

	std::string prefix = "";
	// handle each test case
	for (int i = 0; i < inputvector.size(); ++i) {
		std::string result = handleTestCase(inputvector[i]);
		outfile << prefix << "Case #" << i + 1 << ": " << result;
		//std::cout << prefix << "Case #" << i + 1 << ": " << result;
		prefix = "\n";
	}

	// clean up the I/O streams
	infile.close();
	outfile.flush();
	outfile.close();

	return 0;
}

/*
 * HELPER FUNCTIONS IMPLEMENTATIONS
 */

void tokenize(std::vector<std::string> &buf, std::string s, const char *delimeters) {
	// clear the output vector
	buf.clear();

	// temporary string buffer
	char *tempStr = new char[s.length() + 1];

	// copy to the array
	s.copy(tempStr, s.length(), 0);
	tempStr[s.length()] = NULL; // make it a valid cstring

	char *token = strtok(tempStr, delimeters);

	while (token != NULL) {
		buf.push_back(std::string(token));
		token = strtok(NULL, delimeters);
	}

	// delete the temporary buffer to not allow a memory leak
	delete[] tempStr;
}


/*
0 = -1
I = -i
J = -j
K = -k
*/
char mul(char row, char col) {
	char result;
	switch (row) {
	case '1':
		return col;

	case 'i':
		switch (col) {
		case '1':
			return 'i';
		case 'i':
			return '0';
		case 'j':
			return 'k';
		case 'k':
			return 'J';
		case '0':
			return 'I';
		case 'I':
			return '1';
		case 'J':
			return 'K';
		case 'K':
			return 'j';
		}
	
	case 'j':
		switch (col) {
		case '1':
			return 'j';
		case 'i':
			return 'K';
		case 'j':
			return '0';
		case 'k':
			return 'i';
		case '0':
			return 'J';
		case 'I':
			return 'k';
		case 'J':
			return '1';
		case 'K':
			return 'I';
		}

	case 'k':
		switch (col) {
		case '1':
			return 'k';
		case 'i':
			return 'j';
		case 'j':
			return 'I';
		case 'k':
			return '0';
		case '0':
			return 'K';
		case 'I':
			return 'J';
		case 'J':
			return 'i';
		case 'K':
			return '1';
		}

	case '0':
		switch (col) {
		case '1':
			return mul('1', '0');
		case 'i':
			return mul('1', 'I');
		case 'j':
			return mul('1', 'J');
		case 'k':
			return mul('1', 'K');
		case '0':
			return mul('1', '1');
		case 'I':
			return mul('1', 'i');
		case 'J':
			return mul('1', 'j');
		case 'K':
			return mul('1', 'k');
		}

	case 'I':
		switch (col) {
		case '1':
			return mul('i', '0');
		case 'i':
			return mul('i', 'I');
		case 'j':
			return mul('i', 'J');
		case 'k':
			return mul('i', 'K');
		case '0':
			return mul('i', '1');
		case 'I':
			return mul('i', 'i');
		case 'J':
			return mul('i', 'j');
		case 'K':
			return mul('i', 'k');
		}

	case 'J':
		switch (col) {
		case '1':
			return mul('j', '0');
		case 'i':
			return mul('j', 'I');
		case 'j':
			return mul('j', 'J');
		case 'k':
			return mul('j', 'K');
		case '0':
			return mul('j', '1');
		case 'I':
			return mul('j', 'i');
		case 'J':
			return mul('j', 'j');
		case 'K':
			return mul('j', 'k');
		}

	case 'K':
		switch (col) {
		case '1':
			return mul('k', '0');
		case 'i':
			return mul('k', 'I');
		case 'j':
			return mul('k', 'J');
		case 'k':
			return mul('k', 'K');
		case '0':
			return mul('k', '1');
		case 'I':
			return mul('k', 'i');
		case 'J':
			return mul('k', 'j');
		case 'K':
			return mul('k', 'k');
		}

	}
}

bool isStringChar(std::string &input, char c) {
	char actual;
	if (!isInCache(input)) {
		actual = calcChar(input);
		addToCache(actual, input);
	}
	else {
		actual = calcCache.find(input)->second;
	}

	return actual == c;
}

void getAllCharStrings(std::vector<size_t> &v, std::string &input, char charToLookFor, size_t offset) {
	v.clear();

	char prevChar;
	for (size_t i = 0; i < input.size(); ++i) {
		if (i == 0) {
			prevChar = input[0];
		}
		else {
			prevChar = mul(prevChar, input[i]);
		}

		// compare
		if (prevChar == charToLookFor) {
			v.push_back(i + offset);
		}

		//addToCache(prevChar, input.substr(0, i + 1));
	}

	// v now contains every position that the char to look for terminates at
}

const std::string no = "NO";
const std::string yes = "YES";

std::string solveDijkstraProblem(std::string input) {
	

	std::map<size_t, std::vector<size_t>> ipos_to_jvector;
	std::vector<size_t> j_strings;

	std::vector<size_t> i_strings;
	getAllCharStrings(i_strings, input, 'i', 0);

	for (size_t i = 0; i < i_strings.size(); ++i) {
		size_t position = i_strings[i] + 1;
		if (position < input.size()) {
			std::string jSearchInput = input.substr(position, input.size() - position);
			getAllCharStrings(j_strings, jSearchInput, 'j', position);
			ipos_to_jvector.insert(std::pair<size_t, std::vector<size_t>>(i_strings[i], std::vector<size_t>(j_strings)));
		}
	}

	// check all combinations of strings to see if there is a match
	for (std::map<size_t, std::vector<size_t>>::iterator it = ipos_to_jvector.begin(); it != ipos_to_jvector.end(); ++it) {
		for (size_t i = 0; i < it->second.size(); ++i) {
			size_t position = it->second[i] + 1;
			if (position < input.size()) {
				std::string potentialKString = input.substr(position, input.size() - position);
				if (isStringChar(potentialKString, 'k')) {
					return yes;
				}
			}
		}
	}
	
	// no match found
	return no;
}

std::pair<int, std::string> createPair(std::ifstream &infile) {
	// buffer to hold a line of input
	std::string line;
	// vector of tokens
	std::vector<std::string> tokens;

	// first line of input
	std::getline(infile, line);
	tokenize(tokens, line);
	int len = atoi(tokens[0].c_str()); // unused
	int reps = atoi(tokens[1].c_str());

	// read string
	std::getline(infile, line);

	return std::pair<int, std::string>(reps, line);
}

std::string handleTestCase(std::pair<int, std::string> &pair) {
	std::string concatenatedStr;
	for (int i = 0; i < pair.first; ++i) {
		concatenatedStr += pair.second;
	}

	// solve the problem!
	return solveDijkstraProblem(concatenatedStr);
}

char calcChar(std::string &s) {
	char prevChar;

	for (size_t i = 0; i < s.size(); ++i) {
		if (i == 0) {
			prevChar = s[0];
		}
		else {
			prevChar = mul(prevChar, s[i]);
		}
	}

	return prevChar;
}

void warmUpCache(std::string &s) {
	for (size_t i = s.size() - 2; ; --i) {
		if (i >= 0) {
			if (s.size() < 2) {
				break;
			}
			std::string sub = s.substr(i, s.size() - i);
			if (!isInCache(sub)) {
				addToCache(calcChar(sub), sub);
			}

			if (i == 0) {
				break;
			}
		}
	}
}