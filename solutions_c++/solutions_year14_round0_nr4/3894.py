#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

void test();
void dwar();
void war();

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		test();
	}
}

int n;
double p1[1010], p2[1010];

void test() {
	cin >> n;
	for(int i = 0; i < n; i++) cin >> p1[i];
	for(int i = 0; i < n; i++) cin >> p2[i];

	sort(p1, p1 + n);
	sort(p2, p2 + n);

	dwar();
	cout << " ";
	war();
	cout << "\n";
}

void dwar() {
	int score = 0;
	int i = 0, j = 0;

	for(; i < n; i++) {
		for(; j < n; j++) {
			if(p1[j] > p2[i]) {
				score++;
				j++;
				break;
			}
		}
	}

	cout << score;
}

void war() {
	int score = n;

	int i = 0, j = 0;
	for(;i < n; i++) {
		for(;j < n; j++) {
			if(p1[i] < p2[j]) {
				score--;
				j++;
				break;
			}
		}
	}

	cout << score;
}
