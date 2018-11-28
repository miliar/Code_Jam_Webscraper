#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("A.out");

char val[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int posFind(char check) {
    for (int i = 0; i < 26; i++)
	if (val[i] == check) return i;
}

void printLast(string in) {
    int len = in.length();
    char out[len];
    out[0] = in[0];
    int ascStart = posFind(out[0]);
    for (int i = 1; i < len; i++) {
        char nLet = in[i];
        int ascIn = posFind(nLet);
        if (ascIn < ascStart) out[i] = nLet;
        else {
	    for (int shift = i; shift > 0; shift--)
		out[shift] = out[shift - 1];
	    out[0] = nLet;
	    ascStart = ascIn;
        }
    }
    for (int i = 0; i < len; i++)
	fout << out[i];        
}

int main() {
    int T;
    fin >> T;
    for (int i = 1; i <= T; i++) {
 	string input;
	fin >> input;
	fout << "Case #" << i << ": ";
	printLast(input);
	fout << endl;
    }   
}
