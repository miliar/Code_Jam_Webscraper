#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

const string filein = "B-large.in", fileout = "output.txt";

void print(ofstream &fo, unsigned int i, double t);
bool cookieClickerAlpha(string fin, string fout);
double getMinTime(const double c, const double f, const double x);
void pause();

int main() {
	if (cookieClickerAlpha(filein, fileout)) cout << "There were errors." << endl;
	else cout << "There were no errors. Output is saved in: " << fileout << "." << endl;
	pause();
	return 0;
}

bool cookieClickerAlpha(string fin, string fout) {
	bool error = false;
	ifstream fi;
	fi.open(fin);
	ofstream fo;
	fo.open(fout);
	if (!fi.is_open() || !fo.is_open()) {
		cout << "Error opening file(s).";
		return true;
	} else {
		unsigned int cases;
		fi >> cases;
		for (unsigned int i = 1; i <= cases && !error; i++) {
			double c, f, x;
			fi >> c;
			fi >> f;
			fi >> x;
			error = fi.fail();
			if (!error) print(fo, i, getMinTime(c, f, x));
		}
		fo.close(); fi.close();
		return error;
	}
}

void pause() {
	cin.clear();
	cin.sync();
	cout << "Press Intro to continue...";
	cin.ignore(INT_MAX, '\n');
}

void print(ofstream &fo, unsigned int i, double t) {
	fo << "Case #" << i << ": " << fixed << setprecision(7) << t << endl;
}

double getMinTime(const double c, const double f, const double x) {
	double t_x, t_c, delta, r, r_mod, time;
	r = 2; time = 0;
	bool done = false;
	while (!done) {
		t_x = x / r;
		t_c = c / r;
		delta = t_x - t_c;
		r_mod = r + f;
		if ((x / r_mod) < delta) { // Buy cookie farm.
			time += t_c;
			r = r_mod;
		} else { // Wait until X cookies and return.
			time += t_x;
			done = true;
		}
	}
	return time;
}