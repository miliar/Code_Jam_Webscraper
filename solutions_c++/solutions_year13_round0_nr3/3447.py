#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int main (int argc, char* argv[]) { 
 	ifstream myfile;
	myfile.open (argv[1]);
	int numTests = -1;
	unsigned long long int low, high;
	string line;
	if (!myfile.is_open()) {
	  return -1;
	}
	getline (myfile,line);
	ofstream resultFile;
	resultFile.open ("result.out");
	
	istringstream ( line ) >> numTests;
	
	for (int test = 0; test<numTests; ++test) {
	  getline (myfile,line);
	  istringstream ( line ) >> low >> high;
	  long int count = 0;
	  for (unsigned long long int i = low; i<=high; ++i) {
	    std::string numberStr = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
	    std::string reverseStr = numberStr;
	    std::reverse (numberStr.begin(), numberStr.end());
	    if (numberStr!=reverseStr) continue;
	    double result = sqrt (i);
	    if (fmod (result, 1.0) == 0.0) {
	      std::string numberStr2 = static_cast<ostringstream*>( &(ostringstream() << result) )->str();
	      std::string reverseStr2 = numberStr2;
	      std::reverse (numberStr2.begin(), numberStr2.end());
	      if (numberStr2!=reverseStr2) continue;
	      ++count;
	    }
	  }
	
	  std::cout << std::endl;
	  resultFile << "Case #" << test+1 << ": ";
    resultFile << count << std::endl;
	}
	resultFile.close();
	
  myfile.close();
	return 0;
}
