//============================================================================
// Name        : Dijkstra.cpp
// Author      : Sarah Lutteropp
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>     /* atoi */
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

char compute(char c1, char c2) {
	/*
	 * i = i
	 * j = j
	 * k = k
	 * a = -1
	 * b = 1
	 * c = -i
	 * d = -j
	 * e = -k
	 */

	if (c1 == 'b') return c2;
	if (c2 == 'b') return c1;

	if (c1 == 'e' && c2 == 'i') return 'd';
	if (c1 == 'e' && c2 == 'j') return 'i';
	if (c1 == 'e' && c2 == 'k') return 'b';
	if (c1 == 'e' && c2 == 'a') return 'k';
	if (c1 == 'e' && c2 == 'c') return 'j';
	if (c1 == 'e' && c2 == 'd') return 'c';
	if (c1 == 'e' && c2 == 'e') return 'a';

	if (c1 == 'd' && c2 == 'i') return 'k';
	if (c1 == 'd' && c2 == 'j') return 'b';
	if (c1 == 'd' && c2 == 'k') return 'c';
	if (c1 == 'd' && c2 == 'a') return 'j';
	if (c1 == 'd' && c2 == 'c') return 'e';
	if (c1 == 'd' && c2 == 'd') return 'a';
	if (c1 == 'd' && c2 == 'e') return 'i';

	if (c1 == 'c' && c2 == 'i') return 'b';
	if (c1 == 'c' && c2 == 'j') return 'e';
	if (c1 == 'c' && c2 == 'k') return 'j';
	if (c1 == 'c' && c2 == 'a') return 'i';
	if (c1 == 'c' && c2 == 'c') return 'a';
	if (c1 == 'c' && c2 == 'd') return 'k';
	if (c1 == 'c' && c2 == 'e') return 'd';

	if (c1 == 'a' && c2 == 'i') return 'c';
	if (c1 == 'a' && c2 == 'j') return 'd';
	if (c1 == 'a' && c2 == 'k') return 'e';
	if (c1 == 'a' && c2 == 'a') return 'b';
	if (c1 == 'a' && c2 == 'c') return 'i';
	if (c1 == 'a' && c2 == 'd') return 'j';
	if (c1 == 'a' && c2 == 'e') return 'k';

	if (c1 == 'i' && c2 == 'i') return 'a';
	if (c1 == 'i' && c2 == 'j') return 'k';
	if (c1 == 'i' && c2 == 'k') return 'd';

	if (c1 == 'i' && c2 == 'a') return 'c';
	if (c1 == 'i' && c2 == 'c') return 'b';
	if (c1 == 'i' && c2 == 'd') return 'e';
	if (c1 == 'i' && c2 == 'e') return 'j';

	if (c1 == 'j' && c2 == 'i') return 'e';
	if (c1 == 'j' && c2 == 'j') return 'a';
	if (c1 == 'j' && c2 == 'k') return 'i';

	if (c1 == 'j' && c2 == 'a') return 'd';
	if (c1 == 'j' && c2 == 'c') return 'k';
	if (c1 == 'j' && c2 == 'd') return 'b';
	if (c1 == 'j' && c2 == 'e') return 'c';

	if (c1 == 'k' && c2 == 'i') return 'j';
	if (c1 == 'k' && c2 == 'j') return 'c';
	if (c1 == 'k' && c2 == 'k') return 'a';

	if (c1 == 'k' && c2 == 'a') return 'e';
	if (c1 == 'k' && c2 == 'c') return 'd';
	if (c1 == 'k' && c2 == 'd') return 'i';
	if (c1 == 'k' && c2 == 'e') return 'b';

	return 'x';
}

char computeSecond(char c1, char c2) {
	string allChars = "ijkabcde";
	for (size_t i = 0; i < allChars.size(); i++) {
		if (compute(c1, allChars[i]) == c2) {
			return allChars[i];
		}
	}
	return 'q';
}


int main() {
	string numCases;

	ofstream outfile;
	outfile.open ("output.out");

	string line;
	ifstream myfile("inputDijkstra.txt");
	if (myfile.is_open()) {
		getline(myfile, numCases);
		int n = atoi(numCases.c_str());

		for (int test = 0; test < n; test++) {
			stringstream ss;
			string int1, int2;
			getline(myfile, line);
			ss << line;
			ss >> int1;
			ss >> int2;

			//int l = atoi(int1.c_str());
			int x = atoi(int2.c_str());
			string word;
			getline(myfile, word);

			string fullword;
			for (int i = 0; i < x; i++) {
				fullword.append(word);
			}

			std::vector<char> charUntil;
			for (size_t i = 0; i < fullword.size(); i++) {
				if (i == 0) {
					charUntil.push_back(fullword[0]);
				} else {
					charUntil.push_back(compute(charUntil[i-1], fullword[i]));
				}
			}

			bool found = false;
			for (size_t i = 0; i < fullword.size(); i++) {
				if (found) break;
				if (charUntil[i] == 'i') {
					for (size_t j = i+1; j < fullword.size(); j++) {
						if (found) break;
						if (computeSecond('i', charUntil[j]) == 'j') {
							if (computeSecond(charUntil[j], charUntil[fullword.size()-1]) == 'k') {
								found = true;
							}
						}
					}
				}
			}

			string res = "NO";
			if (found) res = "YES";

			cout << "Case #" << test + 1 << ": " << res << endl;
			outfile << "Case #" << test + 1 << ": " << res << endl;
		}

		myfile.close();
		outfile.close();
	}
	return 0;
}
