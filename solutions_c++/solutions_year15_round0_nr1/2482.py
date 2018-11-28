#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
	int T;
	int results[100] = {0}; // T <= 100
	vector<string> input(100); // Smax <= 1000

	ifstream ifs("A-large.in", ifstream::in);
	// input
	ifs >> T; // lines / # test cases
	for(int it = 0; it<T; it++)
	{
		int Sm = 0;
		ifs >> Sm;
		string S;
		ifs >> S;
		input[it] = S.substr(0, Sm+1);
	}
	// output
	ofstream ofs("A-large.out");
	for(int it= 0; it<T; it++)
	{
		string S = input[it];
		if(S.size() == 1){
			ofs << "Case #" << it+1 << ": " << 0 << endl;
			continue;
		}
		int accumulate = S[0]-'0';
		int friends = 0;
		for(int k = 1; k < S.size(); k++)
		{
			int digit = S[k]-'0';
			if(digit>0 && accumulate < k){
				friends+=(k-accumulate);
				accumulate = k+digit;
			}
			else{
				accumulate += digit;
			}
		}
		ofs << "Case #" << it+1 << ": " << friends << endl;
	}

	return 0;
}