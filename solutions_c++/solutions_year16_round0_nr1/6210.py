//name Yufei Wang

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <iomanip>
#include <math.h>
#include <algorithm>
#include <vector>
#include <unordered_set>
using namespace std;
bool checkfinish(vector<int> digits);
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
	long long int N = 0;
	vector<int> digits(10,0);
	int LastDigit = 0;
	long long int temp = 0;
	int j = 0;

	for (int i = 1; i <= T; ++i)
	{	
		infile>>N;
		j = 0;
		for (int i = 0; i < 10; ++i)
		{
			digits[i] = 0;
		}
		temp = 0;



		while(N != 0) {
			j++;
			temp = j * N;
			while(temp != 0) {
				LastDigit = temp % 10;
				digits[LastDigit] = 1;
				temp = temp/10;
			}
			if(checkfinish(digits)) {
				break;
			}
		}
		if(N == 0) {
			outfile<<"Case #"<<i<<": INSOMNIA"<<endl;	
		}
		else {
			outfile<<"Case #"<<i<<": "<<j*N<<endl;
		}
		
	}


}



bool checkfinish(vector<int> digits) {
	for (int i = 0; i < digits.size(); ++i)
	{
		if(digits[i] == 0)
			return false;
	}
	return true;
}