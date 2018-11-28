#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;


vector<int> tokenize(string str) {
    string buf; // Have a buffer string
    stringstream ss(str); // Insert the string into a stream

    vector<int> tokens; // Create vector to hold our words

    while (ss >> buf)
        tokens.push_back(atoi(buf.c_str()));
	
	return tokens;
}

char convert(int num) {
	int x = (int) 'A' + num;
	return char (x);
}


void getMax(vector<int>& inputs, int& largest, int& secondLargest) {
	int vLargest, vSecondLargest;
	if (inputs[0] > inputs[1]) {
		largest = 0;
		secondLargest = 1;
		vLargest = inputs[0];
		vSecondLargest = inputs[1];
	} else {
		largest = 1;
		secondLargest = 0;
		vLargest = inputs[1];
		vSecondLargest = inputs[0];		
	}
	for (int i = 2; i < inputs.size(); ++i) {
		if (inputs[i] > vLargest) {
			secondLargest = largest;
			largest = i;
			vSecondLargest = vLargest;					
			vLargest = inputs[i];
		} else if (inputs[i] > vSecondLargest) {
			secondLargest = i;
			vSecondLargest = inputs[i];
		}
	}
	
}

int total(vector<int>& inputs) {
	int totalCount = 0;
	for (int i = 0; i < inputs.size(); ++i) {
		totalCount += inputs[i];
	}
	return totalCount;
}

bool isBaseCase(vector<int>& inputs) {
	return total(inputs) == 2;
}

bool valid(vector<int>& inputs) {
	int largest, secondLargest;
	getMax(inputs, largest, secondLargest);
	if (total(inputs) < largest * 2) {
		return false;
	} 
	return true;
}

string smartGreedy(vector<int>& inputs) {
	string answer = "";
	int largest, secondLargest;
	while (true) {
		getMax(inputs, largest, secondLargest);
		if (isBaseCase(inputs)) {
			inputs[largest]--;
			inputs[secondLargest]--;
			answer = answer + convert(largest) + convert(secondLargest);
			return answer;
		} else {
			inputs[largest]--;
			inputs[secondLargest]--;
			if (valid(inputs)) {
				answer = answer + convert(largest) + convert(secondLargest) + " ";				
			} else {
				inputs[secondLargest]++;
				answer = answer + convert(largest) + " ";
			}
		}
	}
	return "";
	
}

string solveProblem(string line, string line2) {
	int N = atoi(line.c_str());
	vector<int> inputs = tokenize(line2);
	return smartGreedy(inputs);
/*	unordered_map<char, int> letters;
	for (int i = 0; i < line.length(); ++i) {
		//letters[line[i]]
		if (letters.find(line[i]) == letters.end()) {
			letters[line[i]] = 1;
		} else {
			letters[line[i]] = letters[line[i]] + 1;
		}
	}



	sort(answers.begin(), answers.end());
	ostringstream oss;
	for (int i = 0 ; i < answers.size(); ++i) {
		oss << answers[i];
	}
	return oss.str();
	*/
	//return to_string(temp);
}


int main(int argc, char* argv[])
{
	std::ifstream infile(argv[1]);
	string line, line2;
	std::getline(infile, line);
	int num = stoi(line);
	for (int i = 1; i <= num; ++i) {
		std::getline(infile, line);
		std::getline(infile, line2);
		cout << "Case #" << i << ": " << solveProblem(line, line2) << endl;
	}
		
		
	return 0;


}