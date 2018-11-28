#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main() {
	
	int t;
	fin >> t;

	for (int k = 1; k <= t; k++){
		int n;
		fin >> n;

		set<int> digi;
		string s = "";
		int count = 1;

		while (digi.size() < 10){
			if (n == 0){
				s = "INSOMNIA";
				break;
			}
			int cc = n * count++;

			s = to_string(cc);

			for (int i = 0; i < s.length(); i++){

				digi.insert(s[i]);
			}
			
		}

		fout << "Case #" << k << ": " << s << endl;
	}


	return 0;
}