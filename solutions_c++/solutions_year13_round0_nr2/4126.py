
#include <istream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <iostream>

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
	size_t sizeX;
	size_t sizeY;
	vector<size_t> board;
	
public:
	size_t valAt(size_t x, size_t y) const {
		return board.at((y * sizeX) + x); 
	}
	friend istream& operator >> (istream& stream, InputData& input);
};

inline istream& operator >> (istream& stream, InputData& input) 
{
	string line;
	size_t value = 0;

	{
		getline(stream, line);
		istringstream is(line);
		is >> input.sizeY;
		is >> input.sizeX;
	}

	for(size_t y=0; y!=input.sizeY; ++y) {
		getline(stream, line);
		istringstream is(line);
		for(size_t x=0; x!=input.sizeX; ++x) {
			is >> value;
			input.board.push_back(value);
		}
	}
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

OutputData Solution::solve(const InputData& input)
{
	OutputData output; 
	
	vector<size_t> rowMaxVal;
	for(size_t y=0; y!=input.sizeY; ++y) {
		size_t maxVal = 0;
		for(size_t x=0; x!=input.sizeX; ++x) {
			maxVal = max(maxVal, input.valAt(x,y));
		}
		rowMaxVal.push_back(maxVal);
	}
	
	vector<size_t> colMaxVal;
	for(size_t x=0; x!=input.sizeX; ++x) {
		size_t maxVal = 0;
		for(size_t y=0; y!=input.sizeY; ++y) {
			maxVal = max(maxVal, input.valAt(x,y));
		}
		colMaxVal.push_back(maxVal);
	}
	
	for(size_t y=0; y!=input.sizeY; ++y) {
		for(size_t x=0; x!=input.sizeX; ++x) {
			size_t val = input.valAt(x,y);
			if(val < rowMaxVal.at(y) && val < colMaxVal.at(x)) {
				output.result = "NO";
				return output;
			}
		}
	}

	output.result = "YES";
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

