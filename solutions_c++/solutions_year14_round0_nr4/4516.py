#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

/**
	Google Code Jam
	Qualification Round 2014
	Problem D. Deceitful War

	https://code.google.com/codejam/contest/2974486/dashboard#s=p3
*/

void read_next_testcase(ifstream &in, int &N, vector<double> &Naomis, vector<double> &Kens) {
	in >> N;
	int i = N;
	double w;

	while (i --) {
		in >> w;
		Naomis.push_back(w);
	}
	i = N;
	while (i --) {
		in >> w;
		Kens.push_back(w);
	}
}

void solve_next_testcase(ifstream &in, ofstream &out, int case_nr) {
	int N;
	vector<double> Naomis, Kens;
	read_next_testcase(in, N, Naomis, Kens);

	sort(Naomis.begin(), Naomis.end());
	sort(Kens.begin(), Kens.end());

	// find war count
	int deceit = N, war = N, ken_index = 0, i, j;
	for (i = 0; i < N && ken_index < N; ++ i) {
		for (j = ken_index; j < N; j ++) {
			if (Kens[j] > Naomis[i]) {
				war --;
				break;
			}
		}
		ken_index = j + 1;
	}

	// find deceit count
	ken_index = 0;
	for (i = 0; i < N ; ++ i) {
		if (Kens[ken_index] > Naomis[i]) {
			deceit --;
		} else {
			ken_index ++;
		}
	}

	out << showpoint << "Case #" << case_nr << ": " << deceit << " " << war << endl;
}

int main () {
	ifstream in;
	ofstream out;

	in.open("D-large.in");
	out.open("output-large.txt");

	int T;
	in >> T;
	int case_nr = 0;
	while (case_nr ++ < T)
		solve_next_testcase(in, out, case_nr);

    in.close();
    out.close();
	return 0;
}