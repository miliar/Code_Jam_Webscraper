#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	  string line;
	  ifstream input("B-large.in");
	  ofstream output("B-large.out");
      string firstLine;
      int lineNumber = 1;
	  vector<char> pancakes;
	  vector<char>::iterator idx;

	  if (input.is_open())
	  {
		  istringstream iss(line);
		  if (input.good())
		  {
			  // jump over first line
			  getline(input,line);
			  while(!input.eof()) {
				  getline(input,line);
				  istringstream buffer(line);
				  if(line == "") break;

				  pancakes.clear();
				  for(int i=0; i<(int)line.length(); i++) {
					  pancakes.push_back(line[i]);
				  }

				  if(find(pancakes.begin(), pancakes.end(), '-') != pancakes.end()) {
					  idx=pancakes.begin();
					  int x=0;
					  int flipped = 0;
					  while(idx < pancakes.end()) {
						  // if differs from first sign
						  if(pancakes.at(0) != *idx) {
							  flipped++;
							  if(pancakes.at(0) == '+') {
								  for(int k=0;k<x;k++) {
									  pancakes.at(k) = '-';
								  }
							  }
							  else if(pancakes.at(0) == '-') {
								  for(int k=0;k<x;k++) {

									  pancakes.at(k) = '+';
								  }
							  }

						  }
						  x++;
						  idx++;
					  }
					  // algorithm didn't reverse anything, because flipping was done for the identical signs
					  // everything is flipped
					  if(pancakes.at(0) == '+') {
						  cout << "Case #" << lineNumber << ": " << flipped << endl;
						  output << "Case #" << lineNumber << ": " << flipped << endl;
					  }
					  else if(pancakes.at(0) == '-') {
						  // turn all once
						  cout << "Case #" << lineNumber << ": " << flipped+1 << endl;
						  output << "Case #" << lineNumber << ": " << flipped+1 << endl;
					  }
				  }
				  else {

					  cout << "Case #" << lineNumber << ": " << 0 << endl;
					  output << "Case #" << lineNumber << ": " << 0 << endl;
				  }
				  lineNumber++;
			  }
		  }
		  input.close();
	  }

	  else cout << "Unable to open file";
	  return 0;
}
