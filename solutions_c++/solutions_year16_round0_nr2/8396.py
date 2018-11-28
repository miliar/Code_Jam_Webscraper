#include <iostream>
#include <vector>
#include <map>
#include <fstream>

using namespace std;

int main() {
	 ifstream fin;
	 ofstream fout;

	 string inname, outname;
	 cin >> inname;
	 int iend = inname.rfind(".");
	 outname = inname.substr(0, iend) + ".out";

	 fin.open(inname);
	 fout.open(outname);
	 cin.rdbuf(fin.rdbuf());
	 cout.rdbuf(fout.rdbuf());

	int T;
	cin >> T;
	//cout << T << endl;

	for (int i = 0; i < T; i++) {
		//cout <<22222<<endl;
		string S;
		cin >> S;
		//cout << S <<endl;
		if (S.empty()) {
			cout << "case #"<< i + 1<<": "<< 0 << endl;
		}
		else {
			char lable = S[0];
			string newString;
			newString = newString + lable;
			//cout << "22222 "<<newString << endl;
			for(int i = 0; S[i] != '\0'; i++) {
				if (S[i] != lable) {
					newString = newString + S[i];
					lable = S[i];
				}

			}
			if (lable == '+') {
				cout << "case #"<< i + 1<<": "<< newString.length() - 1 << endl;
			}
			else {
				cout << "case #"<< i + 1<<": "<< newString.length()<< endl;
			}
		}

	}

	return 0;
}
