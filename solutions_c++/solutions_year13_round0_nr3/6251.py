#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>

using namespace std;

// map<long, int> palindromes;

bool is_palindrome(long p) {
	/*if (palindromes[p] == 2) {
		return false;
	}
	if (palindromes[p] == 1) {
		return true;
	}*/
		
	ostringstream convert;
	convert << p;
	
	string pstr = convert.str();
	long length = pstr.length();
	long middle = length/2;
	
	for (int i=0; i<=middle; i++) {
		if (pstr[i] != pstr[length-i-1]) {
			// palindromes[p] = 2;
			return false;
		}	
	}

	// palindromes[p] = 1;
	return true;	
}

int main(int argc, char *argv[]) {
	ifstream indata ("C-small-attempt0.in");
	ofstream outdata ("C-small-attempt0.out");
	string line;
	long t;
	
	if (indata.is_open()) {
		getline (indata, line);
		istringstream(line) >> t;
		
		for (int i=0; i<t; i++) {
			long a, b;
			
			getline (indata, line);
			istringstream(line) >> a >> b;
			
			long root = sqrtl(a);
			if (a > root*root) {
				root++;
			}
			long palindrome = root*root;
			long pc = 0;
			
			while (b >= palindrome) {
				
				if (is_palindrome(root)) {
					if (is_palindrome(palindrome)) {
						pc++;
					}
				}
				
				root++;
				palindrome = root*root;
			}
			
			outdata << "Case #" << i+1 << ": " << pc << endl;
			cout << "Case #" << i+1 << ": " << pc << endl;
		}
						
		outdata.close();
		indata.close();
	} else {
		cout << "File not found :( " << endl;
	}
}