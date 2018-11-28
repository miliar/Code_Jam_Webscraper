// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <stdint.h>
#include <list>
#define FF(I,N) for(int I=0;I<N;I++)
#define FR(I,N) for(int I=N-1;I>=0;I--)

typedef long long LL;
using namespace std;
const LL INFN = -9223372036854775807; //const LL INFN = (int64_t)1<<63;
const LL INFP = 9223372036854775807; // const LL INFN = (int64_t)1<<62;

int main(int argc, char * argv[]){
		
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		string S;getline(ifh,line);stringstream(line) >> S;
	
		
		//Solution
		std::list<int> mylist;
		mylist.push_back(S[0]);
		FF(i,S.length()-1)
		{
		  if(S[i+1]>=mylist.front())
		    mylist.push_front(S[i+1]);
		  else
		    mylist.push_back(S[i+1]);
		}
		
				
		// Output
		ofh << "Case #"<< t+1 << ": ";
		for (std::list<int>::iterator it=mylist.begin(); it != mylist.end(); ++it)
		    ofh  << (char)*it;
		ofh << endl;
		
		
		cout << "Case #"<< t+1 << ": ";
		for (std::list<int>::iterator it=mylist.begin(); it != mylist.end(); ++it)
		    cout  << (char)*it;
		cout << endl;
	}
return 0;
}



		