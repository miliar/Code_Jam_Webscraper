#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <bitset>
using namespace std;

// just use string indices here
// ++++
// 0123 
string flip_stack (std::string input, int n) 
{
	string output=input;
	for (int i=n; i>=0; --i) {
		if (input[i] == '+') 
			output [n-i] = '-';
		else   
			output [n-i] = '+';
	}
	return output;
}
unsigned solve_problem (std::string input) {
	unsigned count =0;
	for (unsigned i =0; i<input.size()-1; ++i ) {
		if (input[i] != input[i+1]) {
			input = flip_stack(input,i);
			++count;
		}
		
	}
	if (input[input.size()-1] == '-') {
		input = flip_stack(input, input.size()-1);
		++count;
	}
	return count;
}
int main(int argc, char* argv[])
{
  string filename= argv[1];
  ifstream file(filename.c_str());
	int numTests;
	file>>numTests;
	string line;
	unsigned x=1;
  while (file) {
		getline (file, line);
    if(!line.empty()){
			string s1 = line;
			string s2 = flip_stack(line, line.size()-1);
			unsigned sol1 = solve_problem(s1);
			unsigned sol2 = solve_problem(s2)+1;
			unsigned sol = sol1<=sol2 ? sol1: sol2; 
			cout <<"Case #"<<x<<": "<<sol<<endl;	
			++x;
		}
	}
  file.close();
}
