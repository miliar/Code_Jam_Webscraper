#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <algorithm>
#include <vector>

using namespace std;

bool allTrue(bool arr[10]) {
	bool flag = true;
	for (int i = 0; i < 10 && flag; ++i)
		flag = arr[i];
	return flag;
}

long long unsigned int countingSheep(int n) {
	if (n == 0)
		return -1;

	bool arr[10] = {false};
	bool endCase = false;
	int i;
	for (i = 1; !endCase; ++i) {
		endCase = true;
		long long unsigned int x = long long unsigned int(i * n);
		while (x > 0) {
			long long unsigned int rem = x % 10;
			arr[rem] = true;
			endCase = allTrue(arr);
			x /= 10;
		}
	}
	return long long unsigned int(--i * n);
}

int main() {
	ifstream fin("input.in");
	ofstream fout("output.txt");
	if (fin) {
		int t;
		fin >> t;
		if (t < 1 || t > 100)
			fout << "Invalid number of Test Cases!" << endl;
		else {
			int n;
			for (int i = 1; i <= t; ++i) {
				fin >> n;
				fout << "Case #" << i << ":" << "   ";
				if (n >= 0 && n <= 1000000) {
					long long unsigned int ans = countingSheep(n);
					if (ans == -1)
						fout << "INSOMNIA" << endl;
					else
						fout << ans << endl;
				}
				else
					fout << "Invalid Case" << endl;
			}
		}
	}
	else
		fout << "Input File Not Found!" << endl;
	fout.close();

	return 0;
}


/*
int main() {
	ofstream fout("input.in");
	srand (time(NULL));
	int x = 100;
	fout << x << endl;
	srand(time(NULL));
	for (int i = 0; i < x; ++i)
		fout << (rand() % 1000000) << endl;
	fout.close();
}
*/