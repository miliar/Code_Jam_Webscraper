#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

int main(void) {
	int t;
	scanf("%d", &t);
	getchar();

	// Para cada caso de teste.
	for (int tc = 1; tc <= t; tc++) {
		// Construindo vetor v.
		string txt;
		cin >> txt;

		vi v(txt.length());

		for (int i = 0; i < v.size(); i++) {
			if (txt[i] == '-') v[i] = 0;
			else v[i] = 1;
		}

		reverse(v.begin(), v.end());

		// Contando número de manobras.
		int moves = 0;

		for (int i = 0; i < v.size(); i++) {
			if (v[i] == 0) {
				moves ++;

				for (int j = i; j < v.size(); j++) {
					v[j] = (v[j] + 1) % 2;
				}
			}
		}

		// Saída.
		printf("Case #%d: %d\n", tc, moves);
	}

	return 0;
}