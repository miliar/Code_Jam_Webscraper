#include <fstream>
#include <iostream>

using namespace std;
std::ofstream outfile("output.txt");

int max(int N, int no_sen[]) {
	int m = 0;
	for (int i = 1; i < N; i++) {
		if (no_sen[i] > no_sen[m])
			m = i;
	}
	return m;
}

int check_valid(int N, int no_sen[], int t) {
	for (int i = 0; i<N;i++) {
		if (no_sen[i] > t/2)
			return false;
	}
	return true;
}

void solve(int tc, unsigned int N, int no_sen[]) {
	outfile << "Case #" << tc << ":";
	int t = 0;
	for (int i=0; i<N; i++)
		t+=no_sen[i];
	while(t) {
		int m = max(N, no_sen);
		no_sen[m]--;
		t--;
		outfile << " ";
		outfile << (char)(65+m);
		if (!check_valid(N, no_sen, t)) {
			m = max(N, no_sen);
			no_sen[m]--;
			t--;
			outfile << (char)(65+m);
		}
		if (!check_valid(N, no_sen, t)) {
			std::cout << "ERROR\n";
		}
	}
}

int main(int argc, char *argv[]) {
	// read file
	std::ifstream infile(argv[1]);
	unsigned int no_tests;
	unsigned int N;
	infile >> no_tests;
	for (int i = 0; i < no_tests; i++) {
		infile >> N;
		int no_sen[26];
		for (int j = 0; j < N; j++) {
			infile >> no_sen[j];
		}
		solve(i+1, N, no_sen);
		outfile << "\n";
	}
	infile.close();
	outfile.close();
	return 0;
}