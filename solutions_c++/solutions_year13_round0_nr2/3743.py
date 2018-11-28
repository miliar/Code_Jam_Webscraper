#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

int main (int argc, char* argv[]) { 
 	ifstream myfile;
 	const int maxHeight = 100;
	myfile.open (argv[1]);
	int numTests = -1;
	int N, M;
	string line;
	if (!myfile.is_open()) {
	  return -1;
	}
	getline (myfile,line);
	ofstream resultFile;
	resultFile.open ("result.out");
	
	istringstream ( line ) >> numTests;
	std::cout << "Tests " << numTests << std::endl;
	
	for (int test = 0; test<numTests; ++test) {
	  std::vector < std::vector <int> > heights;
	  getline (myfile,line);
	  istringstream ( line ) >> N >> M;
	  std::cout << "N " << N << " M " << M << std::endl;
	  heights.resize (N);
	  for (int n = 0; n<N; ++n) {
	    getline (myfile,line);
	    string buffer;
	    stringstream aij (line);
	    while (aij >> buffer) {
	      heights[n].push_back (atoi (buffer.c_str()));
      }
	  }
	  bool ok = true;
	  for (int n = 0; n<N && ok; ++n) {
	    for (int m = 0; m<M && ok; ++m) {
	      const int val = heights[n][m];
	      for (int nn = 0; nn<N && ok; ++nn) {
	        if (heights[nn][m] > val)
	          for (int mm = 0; mm<M && ok; ++mm) {
	            if (heights[n][mm] > val)
	              ok = false;
	          }
	      } 
	    }
	  }
	  resultFile << "Case #" << test+1 << ": ";
	  if (ok)
	    resultFile << "YES " << std::endl;
	  else	  
  	  resultFile << "NO " << std::endl;
	}
	resultFile.close();
	
  myfile.close();
	return 0;
}
