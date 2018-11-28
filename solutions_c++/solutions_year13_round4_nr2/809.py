#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string s; int n; int p; int test; int could = 0; int guarant = 0;

int d[15];

bool best(int number) {
	int win = 0; int k = 1; int sum = 0;
	while (d[n] - number >= sum + k) {
		sum += k;
		win++; k *= 2;
	}
	if (d[n - win] + 1 <= p) {
		return true;
	} else {
		return false;
	}
}

bool worst(int number) {
	int loos = 0; int k = 1; int sum = 0;
	while (number >= (k + sum)) {
		sum += k;
		loos++; k *= 2;
	}
	if (d[n] - d[n - loos] + 1<= p) {
		return true;
	} else {
		return false;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	d[0] = 1; 
	for (int i = 1; i <= 15; i++) {
		d[i] = d[i - 1] * 2;
	}
	for (int i = 0; i <= 15; i++) {
		d[i]--;
	}
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> n >> p;
		for (int i = d[n]; i >= 0; i--) {
			if (worst(i)) {
				guarant = i; 
				break;
			}
		}
		for (int i = d[n]; i >= 0; i--) {
			if (best(i)) {
				could = i;
				break;
			}
		}
		cout << "Case #" << t << ": " << guarant << " " << could << endl;
	}
}
	
	