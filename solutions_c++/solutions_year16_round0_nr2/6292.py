//name Yufei Wang
#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <iomanip>
#include <math.h>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

int main (int arg, char* argv[])
{
	int T = 0;

	//////////////////////////file reading//////////////////
	string filename;
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1], ios::in);
	outfile.open("result.txt", ios::out);
	if(!infile)
	 {
	  cout <<" cannot open file" ;
	  exit(0);
	  }
	 //////////////////////////file reading//////////////////
	infile >> T;

//unordered_set<long long int> repeat;
	string S;
	int res = 0;
	bool last = true;
	bool current = true;
	for (int i = 1; i <= T; ++i)
	{	
		res = 0;
		infile >> S;
		last = (S[0]=='-')? false:true;
		for (int i = 1; i < S.length(); ++i)
		{
			current = (S[i]=='-')? false:true;
			if(last!=current){
				res++;
			}
			last = current;
		}
		
		if(!last) {
			res++;
		}


		outfile<<"Case #"<<i<<": "<<res<<endl;
		
		
	}


}


