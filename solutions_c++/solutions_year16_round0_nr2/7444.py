#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void flip(string &s, int index) {
	for (int i = 0; i <= index; i++) {
		if (s[i] == '+') s[i] = '-';
		else s[i] = '+';
	}
}

int main()
{
	ifstream input("ulaz.txt");
	ofstream output("izlaz.txt");
	int T;
	string temp;
	getline(input, temp);
	T = stoi(temp);
	int X = 1;
	while (X <= T) {
		int index = 0;
		bool flag = true;
		int c = 0;
		string s;
		getline(input, s);
		while (flag) {
			int maxim = -1;
			for (int i = 0; i < s.size(); i++) if (s[i] == '-' && i > maxim)  maxim = i;
			if (maxim == -1) {
				flag = false;
				break;
			}
			flip(s, maxim);
			c++;
		}
		output << "Case #" << X << ": " << c << endl;
		X++;
	}
}