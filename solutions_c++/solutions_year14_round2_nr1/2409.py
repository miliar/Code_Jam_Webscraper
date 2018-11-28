//program the repeater
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <list>
#include <deque>
#include <algorithm>
#include <numeric>
#include <tokenizer.hpp>  //split function to tokenize strings according to delimiters
//#include <Array2D.hpp> //simple multi-array implementation

using namespace std;

//this method solves the problem
string solve(vector<string> lines, int size) {
	string solution;
	vector<list<char>> words;
	list<char> pattern;
	int changes=0;
	
	//read first line into basic (without repeats)
	pattern.push_back(lines[0][0]);
	for (int i = 1; i < lines[0].size(); ++i) {
		if (lines[0][i] != pattern.back()) {
			pattern.push_back(lines[0][i]);
		}
	}
	for (int i = 0; i < lines.size(); ++i) {
		list<char> c;
		c.assign(lines[i].begin(),lines[i].end());
		words.push_back(c);
	}
	while (!pattern.empty()) {
		if (words.size() == 1) return "Fegla Won";
		if (!all_of(words.begin(), words.end(), [&pattern](list<char> s){
			return (s.front() == pattern.front());
		})) {
			return "Fegla Won";
		}
		char a = pattern.front();
		pattern.pop_front();
		//calculate average of 'a' current symbol
		vector<int> veces;

		for (list<char> x : words) {
			int count = 0;
			while (!x.empty()&&(a == x.front())) {
				count++;
				x.pop_front();
			}
			veces.push_back(count);
		}

		int average = std::round((1.0*std::accumulate(begin(veces),end(veces),0)) / veces.size());

		//remove symbols;
		for (list<char> &x : words) {
			int count = 0;
			while (!x.empty()&&(x.front() == a)) {
				x.pop_front();
				count++;
			}
			changes += (abs(average - count));
		}
		//remove empty strings;
		words.erase(remove_if(begin(words), end(words), [](list<char> x) {return x.empty(); }), words.end());
	}
	if (!words.empty()) return "Fegla Won";
	stringstream ss(solution);
	ss << changes;
	ss >> solution;
	return solution;
}

int main(int argc, char* argv[]) {
	string in, temp, line;
	if (argc<2 || argc>3) {
		cout << "Please use <app> <infile> <outfile>" << '\n';
		return 0;
	}
	in = argv[1];
	string out = (argc == 3) ? argv[2] : "out.txt";
	
	//reading input file
	ifstream myfile(in);
	ofstream myoutfile(out);
	if (myfile.is_open()&&myoutfile.is_open())
	{
		//read first line, with number of problems to solve
		getline(myfile, line);
		int times = stoi(line); //number of use cases
		int count = 0;
		//solve X problems
		while (count<times) {
			getline(myfile, line);
			int n = stoi(line);
			vector<string> entry;
			int rows = n;
			for (int i = 0; i < rows; ++i) {
				getline(myfile, line);
				entry.push_back(line);
			}
			//work with the input file one line each time
			myoutfile << "Case #" << (++count) << ": " << solve(entry,n) << '\n';
			//myoutfile << entry[0] << '\n' << entry[1] << '\n';
		}
		myfile.close();
		myoutfile.close();
	}
	else cout << "Unable to open file\n";
	return 0;
}