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

		set<int> digits;
		string str = "";
		int count = 1;

		while (digits.size() < 10){
			if (n == 0){
				str = "INSOMNIA";
				break;
			}
			int cat = n * count++;

			str = to_string(cat);

			for (int i = 0; i < str.length(); i++){

				digits.insert(str[i]);
			}
			
		}

		fout << "Case #" << k << ": " << str << endl;
	}


	return 0;


}