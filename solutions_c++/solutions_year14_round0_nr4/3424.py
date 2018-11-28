#include <list>
#include <map>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int te = 1; te <= tests; te++) {
		int numbers;
		cin >> numbers;
		vector<float> naomi(numbers);
		for(int i = 0; i < numbers; i++) cin >> naomi[i];
		vector<float> ken(numbers);
		for(int i = 0; i < numbers; i++) cin >> ken[i];
		sort(naomi.begin(), naomi.end(), std::greater<float>());
		sort(ken.begin(), ken.end(), std::greater<float>());
		int idxNaomi = 0, idxKen = 0;
		int normalBest = 0;
		while (idxNaomi < numbers) {
			if (naomi[idxNaomi] > ken[idxKen]) {
				normalBest++;
				idxNaomi++;
			} else {
				idxNaomi++;
				idxKen++;
			}
		}

		idxNaomi = numbers - 1;
		idxKen = numbers - 1;
		int deceit = 0;
		for (int i = 0; i < numbers; i++) {
			if (naomi[idxNaomi] < ken[idxKen]) {
				idxNaomi--;
			} else {
				idxNaomi--;
				idxKen--;
				deceit++;
			}
		}
		cout << "Case #" << te << ": " << deceit << " " << normalBest << endl;
	}
}


