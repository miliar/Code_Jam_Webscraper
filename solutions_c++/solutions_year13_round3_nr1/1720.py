#include <iostream>
#include <string>

#include "debug.h"

using namespace std;

int I, T;
const int L = 100;
int N;
string S;
int size;
bool* mask;
int R;

void clean() {
	S = "";
	R = N = size = 0;
	delete [] mask;
}

void print() {
	cout << "Case #" << I << ": " << R << endl;
}

void read() {
	cin >> S;
	cin >> N;
	size = S.size();
	mask = new bool [size];
}

__forceinline bool is_vowel(char c) {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

void solve() {
	bool found;
	int num;
	for (int i = 0; i<size; i++) {
		mask[i] = is_vowel(S[i]);
	}
	for (int i = 0; i<size; i++) {
		for (int j = i+1; j<size+1; j++) {
			if (j - i < N) continue;
			found = false;
			for (int m = i; m<j; m++) {
				num = 0;
				for (int k = 0; k<N; k++) {
					if (m+k>=j) continue;
					if (!mask[m+k]) num++;
					if (mask[m+k]) break;
				}
				if (num == N) {
					found = true;
					break;
				}
			}
			if (found) R++;
		}
	}
}

void sub_main() {
	cin >> T;
	I = 0;
	while (I++<T) {
		read();
		solve();
		print();
		clean();
	}
}