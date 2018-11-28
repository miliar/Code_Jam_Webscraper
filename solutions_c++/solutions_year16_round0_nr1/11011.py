#include <iostream>
#include <stdio.h>
#include <set>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ofstream myfile;
	myfile.open("ans.txt");
	ifstream myReadFile;
	myReadFile.open("example.txt");
	if (myReadFile.is_open()) {
		long long num_cases;
		myReadFile >> num_cases;
		for (long long h = 0; h < num_cases; h++) {
			unsigned long long n, f;
			set<int> s;
			myReadFile >> n;
			long long i = 0;
			if (n==0) {
				myfile << "Case #" << h + 1 << ": " << "INSOMNIA" << endl;
			} else {
				while (s.size() < 10 && n != 0) {
					long long t = n * i;
					f = t;
					i++;
					while (t) {
						s.insert(t % 10);
						t /= 10;
					}
				}
				myfile << "Case #" << h + 1 << ": " << f << endl;
			}
		}
	}
	return 0;
}
