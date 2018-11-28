#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int N;
	cin >> N; cin.ignore();
	vector<string> tab(N, "");
	for (int i = 0; i < N; i++) {
		getline(cin, tab[i]);
	}

	for (int i = 0; i < N; i++) {
		//on fait les retournements pour chaque element enregistré dans le vector
		int nb_operations = 0;
		int taille_chaine = tab[i].size();
		int j = 0;
		while (j < taille_chaine) {
			if (tab[i][j] == '-') {
				while (tab[i][j] == '-') {
					j++;
				}
				nb_operations++;
			} else {
				while (tab[i][j] == '+') {
					j++;
				}
				//tab[i][j] = -
				if (j < taille_chaine) {
					j++;
					while (tab[i][j] == '-') {
						j++;
					}
					nb_operations += 2;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << nb_operations << "\n";
	}

	return 0;
}