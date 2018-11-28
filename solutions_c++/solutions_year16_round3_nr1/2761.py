#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
	ifstream in("aa.in");
	ofstream out("aa.out");
	int N, ON;
	in >> ON;
	N = ON;
	int v[100];
	char A[26] = { 'A','B','C','D','E','F','G','H', 'I','J','K','L', 'M','N','O','P', 'Q','R','S','T', 'U','V','W','X','Y','Z' };
	while (N--) {
		int n, number, all = 0;
		in >> n;
		for (int temp = 0; temp < n; temp++) {
			in >> number;
			v[temp] = number;
			all += number;
		}
		out << "Case #" << ON - N << ": ";
		while (1) {
			int i = 0;
			int j = 0;
			for (int k = 0; k < n; k++) {
				if (v[j] <= v[k]) {
					if (v[i] <= v[k]) {
						j = i;
						i = k;
					}
					else
						j = k;
				}
			}
			if (all == 2) {
				out << A[j] << A[i];
				break;
			}
			if (all == 3) {
				if (v[i] == 2) {
					out << A[i] << A[i] << " ";
					v[i]--;
					all -= 2;
				}
				else {
					all--;
					out << A[i] << " ";
				}
			}
			else {
				if (v[j] == 1 && v[i] == 2) {
					out << A[i] << A[i] << " ";
					all -= 2;
					v[i]--;
				}
				else {
					out << A[j] << A[i] << " ";
					all -= 2;
					v[j]--;
				}
			}
			v[i]--;
		}
		out << endl;
	}
	return 0;
}