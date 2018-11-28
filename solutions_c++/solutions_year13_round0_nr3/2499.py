/*
ID: cyanophycean314
*/
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <sstream>
#include <algorithm>
using namespace std;

bool checkPal(string num) {
    int i;
    for ( i = 0; i < num.length() / 2 + 1; i++) {
        if (num[i] != num[num.length() - i -1])
            return false;
    }
    return true;
}

int fairSquare(string A, string B) {
	for (int i = 

int main() {
	ifstream fin("fairsquare.in");
	ofstream fout("fairsquare.out");
	
	int N;
	fin >> N;
	
	for (int count = 0; i < N; i++) {
		string A;
		string B;
		fin >> A >> B;
		fout << "Case #" << (count + 1) << ": " << fairSquare(A, B) << endl;