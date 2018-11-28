
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

int main(int argc, char** argv) {
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	// load case number
	fin >> CASE_NUM;
	cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 1; ti <= CASE_NUM; ti++) {
		string S;
		fin >> S;

		list<char> lastWord;
		const char* str = S.c_str();
		char max = str[0];
		lastWord.push_back(str[0]);

		for (int i = 1; i < S.length(); i++) {
			char temp = str[i];
			if (temp < max) {
				lastWord.push_back(temp);
			}
			else {
				lastWord.push_front(temp);
				max = temp;
			}
		}

		fout << "Case #" << ti << ": ";
		for (auto temp : lastWord)
			fout << temp;
		fout << endl;
	}

	fin.close();
	fout.close();
}


