#include <iostream>
#include <fstream>

using namespace std;

long sum(char *a, int till) {
	long s = 0;
	for (long i = 0; i <= till; i++) {
		s += a[i] - '0';
	}
	return s;
}

int main() {
	long t;
	fstream f; f.open("a.txt");
	fstream f2; f2.open("output.txt", ios :: out);
	f >> t;
	//cin >> t;
	int smax;
	long needed;
	char a[1000000];
	long n = t;
	while (t--) {
		f >> smax;
		//cin >> smax;
		f >> a;
		//cin >> a;
		needed = 0;
		for (long i = 1; i <= smax; i++) {
			if (sum(a, i - 1) + needed < i) {
				needed += i - (sum(a, i - 1) + needed);
			}
		}
		f2 << "Case #" << n - t << ": " << needed <<"\n";
		//cout << "Case #" << n - t << ": " << needed << "\n";
	}
	return 0;
}