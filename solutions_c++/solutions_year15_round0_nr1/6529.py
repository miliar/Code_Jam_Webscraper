
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

int main() {
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	int t;
	fin >> t;
	for (int k = 0; k < t; k++)
	{
		int max;
		string inp;
		fin >> max;
		fin.ignore();
		getline(fin, inp);
		int cnum = 0;
		int needed = 0;
		for (int i = 0; i < inp.size(); i++)
		{
			int curp = inp[i] - '0';
			if (curp == 0)
				continue;
			if (cnum >= i)
				cnum += curp;
			else
			{
				needed += i - cnum;
				cnum += (i-cnum) + curp;
			}
		}
		fout << "Case #" << k+1 << ": " << needed << endl;
	}
	cin.get();
	return 0;
}