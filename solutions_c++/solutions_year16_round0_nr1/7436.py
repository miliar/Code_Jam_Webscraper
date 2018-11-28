#include<iostream>
#include<array>
#include<fstream>
using namespace std;

template<typename T, size_t N>
bool checker(array<T, N> check) {
	for (bool b : check) {
		if (!b) return false;
	}

	return true;
}
template<typename T, size_t N>
void marker(array<T, N>& check, int number) {
	if (number == 0) {
		check[0] = 1;
	}
	else {
		while (number != 0) {
			check[number % 10] = 1;
			number /= 10;
		}
	}
	return;
}

int main() {
	ofstream myfile("out.txt");
	ifstream infile("A-large.in");
	int t_count, seed;
	infile >> t_count;
	if (!myfile.is_open()) {
		cout << "File fail.\n"; return -1;
	}
	for (int t = 1; t <= t_count; ++t) {
		bool fail = 0;
		infile >> seed;
		if (seed == 0) fail = 1;
		int cur_val = 0;
		array<bool, 10> incidence_array;
		incidence_array.fill(0);
		while (!checker(incidence_array) && !fail){
			cur_val += seed;
			marker(incidence_array, cur_val);
			if (cur_val < seed) fail = 1;
		}
		if (fail) myfile << "Case #" << t << ": INSOMNIA\n";
		else myfile << "Case #" << t << ": " << cur_val << endl;
	}
}