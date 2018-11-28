#include <vector>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

char flip_single(char c) {
	if(c == '+') return '-';
	if(c == '-') return '+';
	return '=';
}

void flip_it(string &config, int n) {
	int left = 0;
	int right = n;

	while(left < right) {
		swap(config[left], config[right]);
		config[left] = flip_single(config[left]);
		config[right] = flip_single(config[right]);

		left++;
		right--;
	}

	if(left == right) config[left] = flip_single(config[left]);
}

int count_flips(string final_config) {
	string current_config(final_config.size(), '+');

	int flips = 0;
	for(int i = final_config.size() - 1; i >= 0; i--) {
		if(current_config[i] != final_config[i]) {
			flip_it(current_config, i);
			flips++;
		}
	}


	return flips;
}


int main() {

	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int T;
	fin >> T; 

	for(int t = 1; t <= T; t++) {
		string buffer;
		fin >> buffer;

		fout << "Case #" << t << ": "; 

		fout << count_flips(buffer) << endl;
	}

	return 0;
}