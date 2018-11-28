#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> tab(N,0);
	for (int i = 0; i < N; i++) {
		cin >> tab[i];
	}

	vector<bool> chiffres(N, false);

	for (int i = 0; i < N; i++) {
		//Cas numero i :
		if (tab[i] == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA\n";
		}
		else {
			std::set<int> tousla;
			int n = 1;
			while (chiffres[i]!=true) {
				int courant = n* tab[i];
				while (courant != 0) {
					int digit = courant % 10;
					tousla.insert(digit);
					courant = courant / 10;
				}
				if (tousla.size() == 10) {
					chiffres[i] = true;
					cout << "Case #" << i + 1 << ": " << n*tab[i] << "\n";
				}
				n++;
			}
		}
	}
	return 0;
}