#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("out.txt");

void readCase(vector <double> &naomi, vector <double> &ken) {
	int n = 0;
	fin >> n;
	double weight = 0;
	for (int i = 0; i < n; i++) {
		fin >> weight;
		naomi.push_back(weight);
	}
	for (int i = 0; i < n; i++) {
		fin >> weight;
		ken.push_back(weight);
	}
}

void output(vector <pair <int, int>> answer) {
	for (int i = 0; i < answer.size(); i++) {
		fout << "Case #" << i + 1 << ": ";
		fout << answer[i].first << " " << answer[i].second << endl;
	}
}

int war(vector <double> naomi, vector <double> ken) {
	int score = 0, n = naomi.size(), kenMin = 0;
	vector <bool> kenUsed(n, false);
	for (int i = 0; i < n; i++) {
		int j = kenMin;
		while (j < n && (ken[j] < naomi[i] || kenUsed[j])) {
			j++;
		}
		if (j == n) {
			score++;
			kenMin++;
		} else {
			kenUsed[j] = true;
		}
	}
	return score;
}

int dwar(vector <double> naomi, vector <double> ken) {
	int score = 0, n = naomi.size(), kenMin = 0;
	for (int i = 0; i < n; i++) {
		if (naomi[i] > ken[kenMin]) {
			score++;
			kenMin++;
		}
	}
	return score;
}

int main() {
	int cases = 0;
	vector <pair <int, int>> res;
	fin >> cases;
	for (int i = 0; i < cases; i++) {
		vector <double> naomi, ken;
		readCase(naomi, ken);
		pair <int, int> scores(0, 0);
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		scores.first = dwar(naomi, ken);
		scores.second = war(naomi, ken);
		res.push_back(scores);
	}
	output(res);
	return 0;
}