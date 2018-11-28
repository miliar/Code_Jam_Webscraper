#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h> 

using namespace std;
#define HULS_2016_RULZ "gcj 2016"

#define INPUT_FILE  "c:\\cj2016\\B-large.in"
#define OUTPUT_FILE "c:\\cj2016\\B-large.out"

long solve(std::string pencakes){
    	int numberOfFlips = 0;
    	bool flipNeeded = false; 
    	for(int i=pencakes.length()-1; i>=0; i--){
    		if( (pencakes[i] == '+') && !flipNeeded ){continue;}
    		if( (pencakes[i] == '+') && flipNeeded ){
    			for(int j=0; j<=i+1; j++){
    				pencakes[j] = ((pencakes[j] == '-') ? '+' : '-' );
    			}
    			numberOfFlips++;
    			flipNeeded = false;
    		}
    		if( (pencakes[i] == '-') && !flipNeeded ){
    			flipNeeded = true;
    		}
    	}
    	if(flipNeeded){numberOfFlips++;}
    	return numberOfFlips;
    }


int main () {
  string line1;
  ifstream infile;
  infile.open(INPUT_FILE);
  ofstream outfile;
  outfile.open (OUTPUT_FILE);
  if (infile.is_open())
  {
      getline (infile,line1);
      cout << line1 << cout;
	  int numberOfTests = atoi(line1.c_str());
	  cout << numberOfTests << cout;
	  for (int t = 1; t <= numberOfTests; t++) {
          string line ;
          getline (infile,line);
          outfile<< "Case #" << t << ": " <<  solve(line) << endl; ;
      }
  }

  infile.close();
  outfile.close();
  return 0;
}
