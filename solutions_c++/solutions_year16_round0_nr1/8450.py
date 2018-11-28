#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

bool check_all_true(vector<bool> v) {
	for(size_t i = 0; i < v.size(); i++) {
		if(v[i] == false) return false;
	}
	return true;
}

int max_moves = 0;
int max_n = 0;

int numara_oile(int n) {
	if (n == 0) return -1;

	vector<bool> have_digit(10, false);
	int current = n;
	int moves = 0;

	do {
		int x = current;
		while(x > 0) {
			have_digit[x % 10] = true;
			x /= 10;
		}

		current += n;
		moves++;
	} while(!check_all_true(have_digit));

	current -= n;
	moves--;

	if (max_moves <= moves) {
		max_moves = moves;
		max_n = n;
	}
	//fout << n << " -> " << current << " [found in " << moves << " moves]" << endl;

	return current;
}



int main() {

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T; 

	for(int t = 1; t <= T; t++) {

		int n;

		fin >> n;

		fout << "Case #" << t << ": ";
		if(n == 0) {
			fout << "INSOMNIA" << endl;
		} else {
			fout << numara_oile(n) << endl;
		}
	}

	return 0;
}