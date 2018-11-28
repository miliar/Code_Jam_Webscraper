#define IOSTREAM_TO_FSTREAM

#include<iostream>
#include<cmath>
#ifdef IOSTREAM_TO_FSTREAM
#include<fstream>
#endif

using namespace std;

void swap(int &a, int &b) {
	int t = a;
	a = b;
	b = t;
}

int main()
{
#ifdef IOSTREAM_TO_FSTREAM
	ifstream fin;
	fin.open("D-small-attempt2.in");
	cin.rdbuf(fin.rdbuf());
	ofstream fout;
	fout.open("D-small-attempt2.out");
	cout.rdbuf(fout.rdbuf());
#endif
	int n0;
	cin >> n0;
	int x, r, c;
	for (int i0 = 1 ; i0 <= n0 ; i0++) {
		cin >> x >> r >> c;
		cout << "Case #" << i0 << ": ";
		if (x == 1) {
			cout << "GABRIEL" << endl;
			continue;
		}
		if ((r * c) % x != 0) {
			cout << "RICHARD" << endl;
			continue;
		}
		if (r < c) {
			swap(r, c);
		}
		if (r < x || (c <= (double)x / 2.0 && x != 2)) {
			cout << "RICHARD" << endl;
			continue;
		}
		cout << "GABRIEL" << endl;
	}
	return 0;
}
