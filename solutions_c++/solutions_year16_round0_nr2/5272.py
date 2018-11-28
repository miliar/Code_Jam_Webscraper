#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

	int T,steps;
	char firstChar,oppositeChar;
	string S;
	//ifstream fin("input.txt");
	
	ifstream fin("input2.in");
	ofstream fout("output.txt");

	fin >> T;

	for (int i = 0;i < T;i++) {
		fin >> S;
		steps = 0;
		while (S.find("-")!=string::npos) {
			firstChar = S.at(0);
			
			if (firstChar == '-')
				oppositeChar = '+';
			else
				oppositeChar = '-';

			for (int j = 0;j < S.length() && S.at(j)!=oppositeChar;j++) {
				string temp(1, oppositeChar);
				S.replace(j,1,temp);
			}

			steps++;

		}

		cout << "Case #" << i + 1<<": " << steps<<endl;
		fout << "Case #" << i + 1 <<": " << steps << endl;


	}
	system("pause");
	return 0;
}