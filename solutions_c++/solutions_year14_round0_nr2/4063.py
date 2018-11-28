#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

void readCase(double &c, double &f, double &x) {
	fin >> c >> f >> x;
}

void output(vector <double> answer) {
	for (int i = 0; i < answer.size(); i++) {
		fout << "Case #" << i + 1 << ": ";
		fout << fixed << setprecision(8) << answer[i] << endl;
	}
}

double bestTime(double c, double f, double x) {
	if (c >= x) {
		return x / 2.0;
	} else {
		double t = 0, tf = 0;
		double res = 0;
		int farms = 0;
		while (true) {
			double speed = 2.0 + f * farms;
			t = (x - c) / speed;
			tf = x / (speed + f);
			if (t <= tf) {
				return res + x / speed;
			} else {
				res += c / speed;
				farms++;
			}
		}
	}
}

int main() {
	int cases = 0;
	vector <double> res;
	fin >> cases;
	for (int i = 0; i < cases; i++) {
		double c = 0, f = 0, x = 0;
		readCase(c, f, x);
		res.push_back(bestTime(c, f, x));
	}
	output(res);
	return 0;
}