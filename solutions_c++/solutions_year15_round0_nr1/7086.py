#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

int T,S;
char ch;

int main()
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");

    fin >> T;
    for(int i = 0; i < T; i++) {
    	fin >> S;
    	int numAud = 0;
    	int level = 0;
    	int fr = 0;
    	for(int j = 0; j < S+1; j++) {
    		fin >> ch;
    		int val = ch - '0';
    		if (numAud >= level || val == 0) {
    			numAud += val;
			} else {
				fr += (level-numAud);
				numAud += (level-numAud) + val;
			}
			level++;
		}
		fout << "Case #" << i+1 << ":" << " " << fr << endl;
	}
    return 0;
}
