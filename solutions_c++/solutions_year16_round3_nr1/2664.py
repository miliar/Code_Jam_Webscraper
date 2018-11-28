#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;


void main() {
	ifstream fin("A-small-attempt0 (1).in");
	ofstream fout("output.txt");
	ifstream infile;
	//infile.open("input.txt");
	int t , n;
	int x[30];
	fin >> t;
	
	for (int i = 0; i < t; i++)
	{
		fout << endl;
		fin >> n;
		int all = 0;
		for (int j = 0; j < n; j++) {
			fin >> x[j];
			all += x[j];
		}
		fout << "case #" << i + 1 << ":";
		while (all > 0) {
			int max = 0, index1, index2;
			int count = 1;

			for (int j = 0; j < n; j++)
			{
				if (x[j] > max) {
					count = 1;
					max = x[j];
					index1 = j;
					index2 = -1;
				}
				else if (x[j] == max) {
					count = 1 - count;
					index2 = j;
				}
			//	cout << max << "**" << index1 << "**" << index2 << endl;
			}
			if (count == 1)
			{
				x[index1]--;
				char d = index1+65;
				fout << d;
				all--;
			}
			else
			{
				x[index1]--;
				x[index2]--;
				char d = index1 + 65;
				char d2 = index2 + 65;
				fout << d;
				fout << d2;

				all -= 2;
			}
			fout << " ";

		}
	}



	cin.get();
}

