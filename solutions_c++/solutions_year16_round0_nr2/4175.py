
#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;


int main()
{
	bool ar[10]{};
	ofstream mf;
	ifstream rf;
	rf.open("test.txt");
	mf.open("output.txt");

	unsigned long int t;
	string s;
	getline(rf, s);
	t = stoi(s, nullptr, 10);
	for (unsigned long int x = 0; x < t; x++) {
		string s;
		int flag = 1, f=1, itr, y, c=0, c1=0;
		getline(rf, s);
		int len = s.length();
		while (flag) {
			if (s[0] == '+') {
				for (itr = 1; itr < len&&f; itr++) {
					if (s[itr] == '-')f = 0;
				}
				for (y = 0; y < itr&&s[itr-1] != '+'; y++) {
					s[y] = '-';
					
				}
				if (s[itr - 1] != '+')c++;
				for (int j = 0; j < len; j++) {
					if (s[j] == '+')c1++;
				}
				if (c1 == len) {
					flag = 0;
					f = 1;
					continue;
				}
				else {
					f = 1;
					c1 = 0;
					continue;
				}
			}
			else {
				for (itr = 1; itr < len&&f; itr++) {
					if (s[itr] == '+')f = 0;
				}
				for (y = 0; y < itr; y++) {
					s[y] = '+';
					
				}
				c++;
				for (int j = 0; j < len; j++) {
					if (s[j] == '+')c1++;
				}
				if (c1 == len) {
					flag = 0;
					f = 1;
					continue;
				}
				else {
					f = 1;
					c1 = 0;
					continue;
				}
			}
		}
		
		mf << "Case #" << x + 1 << ": " << c<<endl;
	}
	rf.close();
	mf.close();

	return 0;

}