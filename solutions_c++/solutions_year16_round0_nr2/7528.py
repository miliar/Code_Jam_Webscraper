#include<iostream>
#include<array>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

bool checker(vector<bool> check) {
	for (bool b : check) {
		if (!b) return false;
	}
	return true;
}
void flip(vector<bool>& pan, int i, int j) {
	for (; i < j; ++i) {
		pan[i] = !pan[i];
	}

}
int main() {
	ofstream outfile("out.txt");
	ifstream infile("B-large.in");
	if (!outfile.is_open() || !infile.is_open()) {
		cout << "File fail.\n"; return -1;
	}
	int t_count;
	string line;
	infile >> t_count;
	getline(infile, line);
	for (int t = 1; t <= t_count; ++t) {
		int flip_count = 0;
		getline(infile, line);
		vector<bool> pancakes(line.size());
		//outfile << line.size() << endl;
		for (int i = 0; i < line.size(); ++i) {
			pancakes[i] = (line[i] == '+');
		}
		//for (bool i : pancakes) outfile << (i ? "+" : "-"); outfile << endl;
		if (!checker(pancakes)) {
			int back = line.size() - 1;
			while (pancakes[back]) --back;
			++back;
			int start = 0;
			
			
			while (back != 0) {
				start = 0;
				while (pancakes[start]) ++start;
				flip(pancakes, 0, start);
				//outfile << "Flip 0-" << start << endl;
				if (start > 0) ++flip_count;
				flip(pancakes, 0, back);
				//outfile << "Flip 0-" << back << endl;
				++flip_count;
				while (--back >= 0 && pancakes[back]);
				++back;
				//outfile << "New back " << back << endl;
				//for (bool i : pancakes) outfile << (i ? "+" : "-"); outfile << endl;
			}
		}
		
		outfile << "Case #" << t << ": " << flip_count << endl;
	}
}