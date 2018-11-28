#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string filein = "D-large.in", fileout = "output.txt";
const unsigned int W = 1000; // Assign W = 10 (small dataset) or W = 1000 (large dataset).

typedef double arr[W];
typedef bool barr[W];

bool deceitfulWar(string fin, string fout);
bool loadArr(ifstream &fi, arr &arr, unsigned int n);
void sort(arr &arr, unsigned int n);
void init(barr &arr, bool value, unsigned int n);
void pause();
void print(ofstream &fo, unsigned int i, unsigned int dScore, unsigned int nScore);
unsigned int nWar(arr &naomi, arr &ken, unsigned int n);
unsigned int dWar(arr &naomi, arr &ken, unsigned int n);
void findWinners(arr &naomi, arr &ken, barr &m_naomi, barr &m_ken, unsigned int n, unsigned int &score);
void findLosers(arr &naomi, arr &ken, barr &m_naomi, barr &m_ken, unsigned int n);
double getMax(arr &arr, barr &barr, unsigned int n, unsigned int &i);
double getMin(arr &arr, barr &barr, unsigned int n, unsigned int &i);
int forceWithMin(arr &arr, barr &barr, double max, unsigned int n);
bool isEmpty(barr &barr, unsigned int n);

int main() {
	if (deceitfulWar(filein, fileout)) cout << "There were errors." << endl;
	else cout << "There were no errors. Output is saved in: " << fileout << "." << endl;
	pause();
	return 0;
}

bool deceitfulWar(string fin, string fout) {
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
			unsigned int n;
			fi >> n;
			arr naomi;
			arr ken;
			bool error = loadArr(fi, naomi, n);
			if (!error) bool error = loadArr(fi, ken, n);
			if (!error) {
				sort(naomi, n);
				sort(ken, n);
				print(fo, i, dWar(naomi, ken, n), nWar(naomi, ken, n));
			}
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

void print(ofstream &fo, unsigned int i, unsigned int dScore, unsigned int nScore) {
	fo << "Case #" << i << ": " << dScore << " " << nScore << endl;
}

bool loadArr(ifstream &fi, arr &arr, unsigned int n) {
	for (unsigned int i = 0; i < n && !fi.fail(); i++) {
		fi >> arr[i];
	}
	if (fi.fail()) return true; else return false;
}

unsigned int nWar(arr &naomi, arr &ken, unsigned int n) {
	barr m_naomi; barr m_ken;
	init(m_naomi, true, n); init(m_ken, true, n);

	unsigned int score = 0;
	bool done = false;

	while (!done) {
		findWinners(naomi, ken, m_naomi, m_ken, n, score);
		unsigned int i;
		getMax(ken, m_ken, n, i);
		m_ken[i] = false;
		done = isEmpty(m_naomi, n);
		if (!done) {
			i = forceWithMin(naomi, m_naomi, ken[i + 1], n);
			m_naomi[i] = false;
		}
		done = isEmpty(m_naomi, n);
	}
	
	return score;
}

unsigned int dWar(arr &naomi, arr &ken, unsigned int n) {
	barr m_naomi; barr m_ken;
	init(m_naomi, true, n); init(m_ken, true, n);

	unsigned int score = 0;
	bool done = false;

	while (!done) {
		findLosers(naomi, ken, m_naomi, m_ken, n);
		done = isEmpty(m_naomi, n);
		if (!done) {
			unsigned int i;
			getMin(ken, m_ken, n, i);
			m_ken[i] = false;
			getMin(naomi, m_naomi, n, i);
			m_naomi[i] = false;
			score++;
		}
		done = isEmpty(m_naomi, n);
	}

	return score;
}

void init(barr &arr, bool value, unsigned int n) {
	for (unsigned int i = 0; i < n; i++) {
		arr[i] = value;
	}
}

void sort(arr &arr, unsigned int n) {
	for (unsigned int i = 1; i < n; i++) {
		double elem = arr[i];
		unsigned int pos = i - 1;
		bool found = arr[pos] > elem;
		while ((pos > 0) && !found) {
			arr[pos + 1] = arr[pos];
			pos--;
			found = arr[pos] > elem;
		}

		if (found) arr[pos + 1] = elem;
		else {
			arr[1] = arr[0];
			arr[0] = elem;
		}
	}
}

void findWinners(arr &naomi, arr &ken, barr &m_naomi, barr &m_ken, unsigned int n, unsigned int &score) {
	unsigned int j;
	double max_ken = getMax(ken, m_ken, n, j);
	for (unsigned int i = 0; i < n && (naomi[i] > max_ken); i++) {
		if (m_naomi[i]) {
			m_naomi[i] = false;
			score++;
		}
	}
}

void findLosers(arr &naomi, arr &ken, barr &m_naomi, barr &m_ken, unsigned int n) {
	unsigned int j;
	double min_ken = getMin(ken, m_ken, n, j);
	for (int i = n - 1; i >= 0 && (naomi[i] < min_ken); i--) {
		if (m_naomi[i]) {
			m_naomi[i] = false;
			getMax(ken, m_ken, n, j);
			m_ken[j] = false;
		}
	}
}

double getMax(arr &arr, barr &barr, unsigned int n, unsigned int &i) {
	bool exit = false;
	double value;
	for (i = 0; i < n && !exit; i++) {
		if (barr[i]) {
			value = arr[i];
			exit = true;
		}
	}
	i--;
	return value;
}

double getMin(arr &arr, barr &barr, unsigned int n, unsigned int &i) {
	bool exit = false;
	double value;
	for (i = n - 1; i >= 0 && !exit; i--) {
		if (barr[i]) {
			value = arr[i];
			exit = true;
		}
	}
	i++;
	return value;
}

int forceWithMin(arr &arr, barr &barr, double max, unsigned int n) {
	unsigned int tmp_i;
	bool found = false;
	int i;
	for (i = n - 1; i >= 0 && !found; i--) {
		if (arr[i] > max && barr[i]) found = true;
	}
	
	if (found) {
		i++;
		return i;
	} else {
		getMax(arr, barr, n, tmp_i);
		return tmp_i;
	}
	
}

bool isEmpty(barr &barr, unsigned int n) {
	bool empty = true;
	for (unsigned int i = 0; i < n && empty; i++) {
		if (barr[i]) empty = false;
	}
	return empty;
}