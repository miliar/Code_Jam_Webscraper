#include <fstream>
#include <list>
using namespace std;

int get_war_score(list<double> naomis, list<double> kens) {
	int score = 0;
	
	while (naomis.size() > 0) {
		if (naomis.back() < kens.back()) kens.pop_back();
		else {
			kens.pop_front();
			score++;
		}
		naomis.pop_back();
	}

	return score;
}

int get_deceit_war_score(list<double> naomis, list<double> kens) {
	int score = 0;

	while (naomis.size() > 0) {
		if (naomis.front() < kens.front()) kens.pop_back();
		else {
			kens.pop_front();
			score++;
		}
		naomis.pop_front();
	}

	return score;
}

int main(int argc, char** argv) {
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);

	int T; ifile >> T;
	for (int tc = 1; tc <= T; tc++) {
		int n; ifile >> n;

		list<double> naomis;
		for (int i = 0; i < n; i++) {
			double bw; ifile >> bw;
			naomis.push_back(bw);
		}

		list<double> kens;
		for (int i = 0; i < n; i++) {
			double bw; ifile >> bw;
			kens.push_back(bw);
		}

		naomis.sort();
		kens.sort();

		int ws = get_war_score(naomis, kens);
		int dws = get_deceit_war_score(naomis, kens);

		ofile << "Case #" << tc << ": " << dws << " " << ws << endl;
	}

	return 0;
}