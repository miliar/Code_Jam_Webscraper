#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

double Vn1[1001], Vk1[1001];

int main () {
	ios::sync_with_stdio(0);

	int T;
	int N;
	double value;
	int y, z;
	int fim;
	int fimn, fimk;

	cin >> T;

	for (int w = 0; w < T; w++) {

		y = z = 0;

		cin >> N;

		

		for (int i = 0; i < N; i++) {
			cin >> value;
			Vn1[i] = value;
		}
		for (int i = 0; i < N; i++) {
			cin >> value;
			Vk1[i] = value;
		}

		sort(Vn1, Vn1 + N);
		sort(Vk1, Vk1 + N);

		//Deceitful War

		fimn = fimk = N - 1;

		for (int i = 0; i < N; i++)

			if (Vn1[fimn] > Vk1[fimk]) {
				y++;
				fimn--;
				fimk--;
			}
			else {
				fimk--;
			}

		//War

		fim = N - 1;


		for (int i = 1; i <= N; i++)
			if (Vn1[N - i] > Vk1[fim])
				z++;
			else
				fim--;
		

		cout << "Case #" << w + 1 << ": ";
		cout << y << " " << z << '\n';

			// for (int i = 0; i < N; i++)
			// 	cout << Vn1[i] << " ";
			// cout << '\n';
			// for (int i = 0; i < N; i++)
			// 	cout << Vk1[i] << " ";
			// cout << '\n';
	}

	return 0;
}