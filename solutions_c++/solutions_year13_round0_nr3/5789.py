#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int palindrome(int n) {
	string s;
	ostringstream convert;
	convert << n;
	s = convert.str();
	int l = s.length();
	for (int i = 0; i < l / 2; i++)
		if (s[i] != s[l - 1 - i])
			return 0;
	return 1;
}
 
int main()
{
	ifstream infile;
	infile.open("C-small.in");
	ofstream outfile;
	outfile.open("C-small.out");

	string line;
	int CaseNum, A, B, num;
	istringstream stream;
	getline(infile, line);
	stream.str(line);
	stream >> CaseNum;
	
	for (int i = 0; i < CaseNum; i++) {
		num = 0;
		istringstream stream1;
		getline(infile, line);
		stream1.str(line);
		stream1 >> A >> B;
		for (int p = sqrt(A - 1) + 1; p <= sqrt(B); p++) {
			if (palindrome(p) == 1 && palindrome(p * p) == 1) {
				num++;
			}
		}

		ostringstream ss;
		ss << "Case #" << (i + 1) << ": " << num << '\n';
		outfile << ss.str(); 
	}


	infile.close();
	outfile.close();
  	return 0;
}
