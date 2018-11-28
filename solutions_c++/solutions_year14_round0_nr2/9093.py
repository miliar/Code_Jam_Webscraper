#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

double time_to_cookies(double X, double rate) {
  return X / rate;
}  

int main(int argc, char** argv) {
	char file_name[1024];
	sprintf(file_name, "%s", argv[1]);

	ifstream inFile;

	inFile.open(file_name);
	if(!inFile) {
		cerr << "Error reading input file\n";
		exit(1);
	}

	int total_testcases;
	inFile >> total_testcases;

	for(int i = 0; i < total_testcases; ++i) {
    double elapsed = 0.0;
    double C, F, X;

    inFile >> C;
    inFile >> F;
    inFile >> X;
    //cerr << "{" << C << ", " << F << ", " << X << "}" << endl;

    double cookies = 0.0;
    double rate = 2.0; // Cookies per second

    bool done = false;
    //for(int j = 0; j < 1000 && !done ; ++j) {
    while ( !done) {
     
      double stopnow = elapsed + time_to_cookies(X, rate);
      double stopnext = elapsed + time_to_cookies(C, rate) + time_to_cookies(X, rate + F);
      //cerr << "stopnow: " << stopnow << ", stopnext: " << stopnext << endl;
      if (stopnow <= stopnext) {
        elapsed = stopnow;
        done = true;
        break;
      }
      else {
        /*cerr << "Cookies: " << elapsed + time_to_cookies(X, rate)
             << " vs "
            << elapsed 
              + time_to_cookies(C, rate)
              + time_to_cookies(X, rate + F) << endl; 
        cerr << "\t elapsed: " << elapsed << endl;
*/
        // How long will it take to b
        double secs = C/rate;
        
        elapsed += secs;
        rate += F;
      }
    }
		//cout << "Case #" << i+1 << ": " << elapsed << endl ;
    printf("Case #%d: %.7f\n", i+1, elapsed);
	}

}
  
