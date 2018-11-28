#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-OutputL.txt");
	int T; fin >> T;
	for (int t = 1; t <= T; t++) {
		string pancakes; fin >> pancakes;
		int count = 0;
		char last = pancakes[0];
		for (int i = 1; i < pancakes.length(); i++) {
			if (pancakes[i] != last)
				count++;
			last = pancakes[i];
		}
		if (pancakes[pancakes.length()-1] == '-') {
			count++;
		}
		cout << "Case #" << t << ": " << count << endl;
		fout << "Case #" << t << ": " << count << endl;
	}
	fin.close();
	fout.close();
	system("pause");//remove
}
