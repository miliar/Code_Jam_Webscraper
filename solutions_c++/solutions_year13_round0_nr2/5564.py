#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <sstream>
using namespace std;

std::vector<int> vsplice(string inString) {
	std::vector<int> outVector;
	string word;
	stringstream stream(inString);
	while( getline(stream, word, ' ') ) {
		outVector.push_back(atoi(word.c_str()));
	}

	return outVector;
}

int main() {
	// read file, create vector
  ifstream inFile("B-large.in");
  ofstream outFile("B-large.out");
  string line;
  std::vector<string> inFileVector;
  if(inFile.is_open()) {
    while(inFile.good()) {
      getline(inFile, line);
      inFileVector.push_back(line);
//			cout << inFileVector.back() << endl;
    }
  }
	
	// splice number of tests
  int T = atoi(inFileVector.front().c_str());
  inFileVector.erase(inFileVector.begin());

	// splice test cases into NxM declaration and matrix arrays
  for(int t = 1; t <= T; t++) {
		// write the NxM vector
		std::vector<int> NxM = vsplice(inFileVector.front());
		int N = NxM.front();
		int M = NxM.back();
		inFileVector.erase(inFileVector.begin());
		// write the matrix
		int Matrix[N][M];	
		for(int n = 0; n < N; n++) {
			std::vector<int> vrow = vsplice(inFileVector.front());
			inFileVector.erase(inFileVector.begin());
			for(int m = 0; m < M; m++) {
				Matrix[n][m] = vrow[m];
//				cout << Matrix[n][m] << " ";
			}
//			cout << endl;
		}
//		cout << endl;

		// run through all cross arrays looking for not max condition
		bool isNotMax = false;
		for(int n = 0; n < N; n++) {
			for(int m = 0; m < M; m++) {
//				cout << " " << Matrix[n][m] << endl;
				// create crossed arrays
				bool isNotHMax = false;
				bool isNotVMax = false;
				int vray[N];
				for(int i = 0; i < N; i++) { vray[i] = Matrix[i][m]; }
				int hray[M];
				for(int j = 0; j < M; j++) { hray[j] = Matrix[n][j]; }
				// determine if max vert
				for(int i = 0; i < N; i++)
				{
//					cout << vray[i] << endl; 
					if(Matrix[n][m] < vray[i]) { isNotVMax = true; break; }
				}
				// determine if max horiz
				for(int j = 0; j < M; j++)
				{
//					cout << hray[j] << " "; 
					if(Matrix[n][m] < hray[j]) { isNotHMax = true; break; }
				}
//				cout << endl;
				// if not HMax and VMax, then NotMax is true and it's impossible to mow
				if(isNotHMax && isNotVMax) { isNotMax = true; break; }
			}
			if(isNotMax) { break; }
		}
		if(isNotMax) { outFile << "Case #" << t << ": " << "NO\n"; }
		else { outFile << "Case #" << t << ": " << "YES\n"; }
	}
	return 0;
}
