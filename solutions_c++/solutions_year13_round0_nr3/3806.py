
#include <istream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

#define LOG(text) //(cout << text << endl)


// - Helpers ------------------------------------------------------------------

template<class T> inline T toNum(const string& str) 
{
	stringstream ss(str);
	T value;
	ss >> value;
	return value;
}

template<class T> inline string toStr(const T& value) 
{
	stringstream ss;
	ss << value;
	return ss.str();
}


// - InputData ----------------------------------------------------------------

class InputData
{
public:
	size_t numA;
	size_t numB;
	
public:
	friend istream& operator >> (istream& stream, InputData& input);
};

inline istream& operator >> (istream& stream, InputData& input) 
{
	string line;

	getline(stream, line);
	istringstream is(line);
	is >> input.numA;
	is >> input.numB;
	return stream;
}


// - OutputData ---------------------------------------------------------------

class OutputData
{
public:
	string result;

public:
	friend ostream& operator << (ostream& stream, OutputData& outputData);
};

inline ostream& operator << (ostream& stream, OutputData& outputData) 
{
	stream << outputData.result;
	return stream;
}


// - Input --------------------------------------------------------------------

class Input
{
public:
	vector<InputData> data;

public:
	friend istream& operator >> (istream& stream, Input& input);
};

inline istream& operator >> (istream& stream, Input& input) 
{
	string line;
	getline(stream, line);
	size_t count = toNum<size_t>(line);

	for(size_t i=0; i<count; ++i) {
		LOG("parsing " << i << "/" << count);
		InputData inputData;
		stream >> inputData;
		input.data.push_back(inputData);
	}

	return stream;
}


// - Output -------------------------------------------------------------------

struct Output 
{
public:
	vector<OutputData> data;

public:
	friend ostream& operator << (ostream& stream, Output& output);
};

inline ostream& operator << (ostream& stream, Output& output)
{
	for(size_t i=0; i!=output.data.size(); ++i) {
		LOG("outputting " << i << "/" << output.data.size());
		stream << "Case #" << (i+1) << ": " << output.data.at(i) << std::endl;
	}
	return stream;
}


// - Solution -----------------------------------------------------------------

struct Solution
{
public:
	void solve(const Input& input, Output& output);
	OutputData solve(const InputData& input);
};

void Solution::solve(const Input& input, Output& output)
{
	for(size_t i=0; i!=input.data.size(); ++i) {
		LOG("solving " << i << "/" << input.data.size());
		OutputData outputData = solve(input.data.at(i));
		output.data.push_back(outputData);
	}
}

inline bool isPalindrome(size_t val) {
	
	int digits = static_cast<size_t>(log10(static_cast<double>(val)))+1;
	int divL = static_cast<int>(pow(10.0, digits-1)); 
	int divR = 1;

	if(digits > 1) {
		while(divL > divR) {
			if( ((val / divL) % 10) != ((val / divR) % 10) ) {
				return false;
			}
			divL /= 10;
			divR *= 10;
		}
	}
	return true;
}

inline bool isSquarePalindrome(size_t val) {
	size_t t = static_cast<size_t>(floor(sqrt(static_cast<double>(val)) + 0.5));
	if(t*t == val && isPalindrome(t)) {
		return true;
	} else {
		return false;
	}
}

OutputData Solution::solve(const InputData& input)
{
	OutputData output;
	vector<size_t> palindromes;
	for(size_t x=input.numA; x<=input.numB; ++x) {
		size_t val = x;
		if(isPalindrome(val)) {
			palindromes.push_back(val);
		}
	}

	vector<size_t> squares;
	for(size_t x=0; x!=palindromes.size(); ++x) {
		size_t val = palindromes.at(x);
		if(isSquarePalindrome(val)) {
			squares.push_back(val);
		}
	}

	output.result = toStr(squares.size());
	return output;
}


// - main ---------------------------------------------------------------------

int main(int argc, char* argv[])
{
	string inputFileName = "input.in";
	string outputFileName = "output.out";
	if(argc == 2) {
		inputFileName = argv[1];
	}

	// Input
	LOG("parsing: " << inputFileName);
	ifstream inputFile(inputFileName);
	if(!inputFile) {
		LOG("Could not open " << inputFileName);
		return 1;
	}

	Input input;
	inputFile >> input;
	
	// Solve
	Output output;
	Solution solution;
	solution.solve(input,output);
	
	// Output
	LOG("outputting: " << outputFileName);
	ofstream outputFile(outputFileName);
	if(!outputFile) {
		LOG("Could not open " << outputFileName);
		return 1;
	}
	
	outputFile << output;
	cout << output;

	//LOG(output);
	
	LOG("Completed");
	return 0;
}

