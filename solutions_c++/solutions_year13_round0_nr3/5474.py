#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
bool isPalindrome(string s) {
	for(int i=0,j=s.size()-1;i<j;++i,--j)
		if(s[i]!=s[j]) return false;
	return true;
}
int main(int argc, char* argv[]) {
	string fName=argv[1];
	string fNameOut=fName;
	fNameOut.insert(fName.rfind('.'),"_r");
	ifstream rFile(fName.c_str());
	ofstream wFile(fNameOut.c_str());
	int T;
	rFile >> T;
	for(int t=0;t<T;++t) {
		int A,B;
		rFile >> A >> B;
		int c=0;
		for(int i=A;i<=B;++i) {
			float tt=sqrt(i);
			if(floorf(tt) == tt) {
				stringstream ss;
				ss << tt;
				if(isPalindrome(ss.str())) {
					stringstream ss2;
					ss2 << i;
					if(isPalindrome(ss2.str()))
						c++;
				}
			}
		}
		wFile << "Case #" << (t+1) << ": " << c << endl;

	}
	rFile.close();
	wFile.close();
	return 0;
}
