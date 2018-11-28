#include <iostream>
#include <vector>

using namespace std;

int matrix[4][4];
int v1[4];
int v2[4];


int main () {
	ios::sync_with_stdio(0);

	int T;
	int a1, a2;
	int value;
	int cont;

	cin >> T;

	for (int z = 0; z < T; z++) {
		
		cont = 0;

		cin >> a1;
		a1--;

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> value;
				matrix[i][j] = value;
			}

		for (int i = 0; i < 4; i++)
				v1[i] = matrix[a1][i];

		cin >> a2;
		a2--;

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> value;
				matrix[i][j] = value;
			}

		for (int i = 0; i < 4; i++)
				v2[i] = matrix[a2][i];

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (v1[i] == v2[j]) {
					value = v1[i];
					cont++;
				}

		cout << "Case #" << z + 1 << ": ";
		
		if (cont == 0)
			cout << "Volunteer cheated!\n";
		else if (cont == 1)
			cout << value << '\n';
		else
			cout << "Bad magician!\n";
	}
	return 0;
}