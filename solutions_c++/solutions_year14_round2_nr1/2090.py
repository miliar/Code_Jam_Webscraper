#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <iomanip>

using namespace std;


int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("result.txt");

	int times;

	fin >> times;

	for (int i = 0; i < times; i++){
		string a, b;
		int numbers;
		fin >> numbers;
		fin >> a;
		fin >> b;
		vector <char> aa, bb;
		vector <int> aa1, bb1;
		int last_one = 0;
		for (int j = 0; j < a.length(); j++){
			if (aa.size() == 0 || aa[aa.size() - 1] != a[j]){
				aa.push_back(a[j]);
				if (aa.size() != 0){
					aa1.push_back(j - last_one);
					last_one = j;
				}
			}
			if (j == a.length() - 1){
				aa1.push_back(j - last_one);
			}
		}
		last_one = 0;
		for (int j = 0; j < b.length(); j++){
			if (bb.size() == 0 || bb[bb.size() - 1] != b[j]){
				bb.push_back(b[j]);
				if (bb.size() != 0){
					bb1.push_back(j - last_one);
					last_one = j;
				}
			}
			if (j == b.length() - 1){
				bb1.push_back(j - last_one);
			}
		}
		if (aa!=bb){
			fout << "Case #" << i + 1 << ": Fegla Won" << endl;
		}
		else{
			int c=0;
			int d;
			for (int j = 0; j < aa1.size(); j++){
				d = aa1[j] - bb1[j];
				if (d < 0){
					d = -d;
				}
				c += d;
			}
			fout << "Case #" << i + 1 << ": " << c << endl;
		}
	}
	fin.close();
	fout.close();
	system("PAUSE");
	return 0;
}

