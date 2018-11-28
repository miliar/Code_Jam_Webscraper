
#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;


int main()
{

	ofstream mf;
	ifstream rf;
	rf.open("test.txt");
	mf.open("output.txt");

	int t;
	string s;
	getline(rf, s);
	t = stoi(s, nullptr, 10);
	for (int x = 0; x < t; x++) {
		getline(rf, s);
		string s1 = s;
		char ch;
		ch = s[0];
		s1[0] = s[0];
		for (int i = 1; i < s.length(); i++) {
			if (s[i] >= ch) {
				for (int j = i; j > 0; j--) {
					s1[j] = s1[j - 1];
				}
				s1[0] = s[i];
				ch = s[i];
			}
			else {
				s1[i] = s[i];
			}
		}
		mf << "Case #" << x + 1 << ": " << s1 << endl;
	}
	rf.close();
	mf.close();

	return 0;

}