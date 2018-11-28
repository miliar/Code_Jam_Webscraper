/*
ID: paelletadecaragols@gmail.com
PROG: Fair and Square
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

int proofCases, lowRange, upRange, validCases;
ifstream fin;
ofstream fout;

bool isPalindromic(int num);
bool isSquare(int num);

int main(){
	int i, j;

	fin.open("C-small-attempt0.in");
        fout.open("C-small-attempt0.out");

        fin >> proofCases;

        for(i=0; i<proofCases; i++){
		fin >> lowRange;
		fin >> upRange;
		validCases = 0;
		for(j=lowRange; j<upRange+1; j++){
			if(isPalindromic(j) and isSquare(j)) validCases++; 
		}
		fout << "Case #" << i+1 << ": " << validCases << endl;
	}
	
}

bool isPalindromic(int num){
	stringstream ss;
	ss << num;
	string s = ss.str();
        int i, j = s.length()-1;
        for(i=0; i<(s.length()/2); i++){
                if(s[i] != s[j-i]) return false;
        }
        return true;
}

bool isSquare(int num){
	int root = (int) sqrt(num);
	if(!isPalindromic(root))
		return false;
	else
 		return num == root * root;
}
