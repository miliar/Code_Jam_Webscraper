#pragma once
#include <fstream>
#include <conio.h>
#include<string>
using namespace std;

void flip(int index, string S) {
	char temp;
	for (int i = 0; i <= index; i++) {
		temp = S[i];
		S[i] = S[index - i];
		S[index - i] = temp;
	}
	for (int i = 0; i <= index; i++) {
		if (S[i] == '+')
			S[i] = '-';
		else
			S[i] = '+';
	}
}

int main() {
	ifstream fin("pancake_small.in");
	ofstream fout("pancake_small.out");
	int T, size, count;
	char first_char;
	string S;
	fin >> T;
	getline(fin, S);//flush out newline
	for (int i = 0; i < T; i++) {
	//	fin >> first_char; //flush out newline
		count = 0;
		getline(fin, S);
		size = S.length();
		first_char = S[0];
		for (int j = 1; j < size; j++) {
			if (S[j] == first_char) //continue till a new cake different from first cake encountered
				continue;
			flip(j - 1, S); //flip all before the new different cake.
			count++;
			first_char = S[j]; //all elements before new different cake will now be same as new cake
		}
		if (S[size - 1] == '-') //if a final flip required?
			count++;
		fout << "Case #"<<i+1<<": "<<count<<endl;
	}
	fin.close();
	fout.close();
}