#include "CJUtils.cpp"

const string INPUT_FILE = "C-small-attempt0.in";
const string OUTPUT_FILE = "C-small-attempt0.out";

string doTestCase(ifstream& infile, vector<size_t>& precomputedFairSquares) {
	
	string line;
	stringstream sstr;
	getline(infile, line);
	sstr.str(line);
	size_t lower, upper;
	sstr >> lower >> upper;

	

	// lower_bound() retutrns an iterator pointing to the first element in the range
	// that does not compare less than val
	// lower_bound(v.begin(), v.end(), 20);

	// Returns an iterator pointing to the first element in the range [first, last) 
	// which compares greater than val.
	// upper_bound(v.begin(), v.end(), 20);

	vector<size_t>::iterator lowerIter = lower_bound(precomputedFairSquares.begin(),
		precomputedFairSquares.end(), lower);
	vector<size_t>::iterator upperIter = upper_bound(precomputedFairSquares.begin(),
		precomputedFairSquares.end(), upper);

	return IntegerToString(upperIter - lowerIter);
}

int main() {
	
	ifstream infile(INPUT_FILE.c_str());
	if (!infile.good()) {
		cout << "Error opening input file." << endl;
		return -1;
	}
	ofstream outfile(OUTPUT_FILE.c_str());

	// Open the precomputed file.
	// Should be 39 numbers.
	ifstream precompute("fairSquare-precompute.txt");
	if (!precompute.good()) {
		cout << "Error opening precomputed file." << endl;
		return -1;
	}
	vector<size_t> precomputedFairSquares;
	while (precompute.good()) {
		string line;
		getline(precompute, line);
		if (!line.empty()) {
			precomputedFairSquares.push_back(StringToInteger(line));
		}
	}

	cout << "Size of precomputed = " << precomputedFairSquares.size() << endl;


	string line;
	// Read the number of test cases
	getline(infile, line);
	size_t T = StringToInteger(line);
	cout << "Test cases " << T << endl;
	for (size_t i = 0; i < T; ++i) {
		cout << "Doing test case " << i + 1 << endl;
		string answer = doTestCase(infile, precomputedFairSquares);
		outfile << "Case #" << i + 1 << ": " << answer << endl;
	}

	getline(cin, line);
	return 0;
}