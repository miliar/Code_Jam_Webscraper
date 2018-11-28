//============================================================================
// Name        : codejam.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	  string line;
	  ifstream input("A-large.in");
	  ofstream output("A-large.out");
      string firstLine;
	  int N;
      int lineNumber = 1;
	  vector<int> seenNumbers;

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
				  buffer >> N;
				  int origN = N;
				  if(N == 0) {
					  cout << "Case #" << lineNumber << ": INSOMNIA" << endl;
					  output << "Case #" << lineNumber << ": INSOMNIA" << endl;
				  }
				  else {
					  int round = 1;
					  seenNumbers.clear();
					  while(seenNumbers.size() < 10) {
						  int tmpN = N;
						  while(tmpN) {
							  int newNumber = tmpN % 10;
							  if(find(seenNumbers.begin(), seenNumbers.end(), newNumber) == seenNumbers.end()) {
								  if(seenNumbers.size() == 9) {

									  cout << "Case #" << lineNumber << ": " << N << endl;
									  output << "Case #" << lineNumber << ": " << N << endl;
								  }
								  seenNumbers.push_back(newNumber);
							  }
							  tmpN /= 10;
						  }
						  round++;
						  N = origN*round;
					  }
				  }
				  lineNumber++;
			  }
		  }

		  input.close();
	  }

	  else cout << "Unable to open file";
	  return 0;
}
