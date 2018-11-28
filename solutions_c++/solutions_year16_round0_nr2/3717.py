#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T;
int S;
string temp;

int main() {
	ifstream fin;
	fin.open("B-large.in");
	fin >> T;
	freopen("B-large.out", "w", stdout);

	for(int i = 0; i < T; i++) {
		fin >> temp;
		char last = 'a';
		int total = 0;
		for(int j = 0; j < (int) temp.length(); j++) {
			if(temp.at(j) != last) {
				total++;
				last = temp.at(j);
			}
		}
		if(temp.at(temp.length()-1) == '+') total--;
		cout << "Case #" << i+1 << ": " << total << endl;
	}



	return 0;
}