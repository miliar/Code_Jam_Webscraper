#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main() {

	int T, N;
	int i, q;
	int arr[10];
	int g;
	int x = 0;
	int y = 0;
	int copy;
	int mult;
	string forever = "INSOMNIA";

	ifstream inFile;
	inFile.open("A-large.in");

	ofstream outFile;
	outFile.open("output.txt");

	inFile >> T;


	for (i = 0; i < T; i++) {

		inFile >> N;
	
		g = 0;
		mult = 1;
		copy = N;
		do {
			if (mult == 1000000000)
				break;


			mult++;
			while (N != 0) {

				if (g == 0) {
					arr[g] = N % 10;
					g++;
				}

				if (y > 0) {
					for (q = 0; q < g; q++) {

						if (arr[q] == N % 10) {
							x++;
						}
					}

					if (x == 0) {
						arr[g] = N % 10;
						g++;
					}
				}

				x = 0;
				y = 1;
				N /= 10;

			}

			if (g == 10) {
				mult--;
				N = copy;
				N = N * mult;
			}
				N = copy;
				N = N * mult;
		

		} while (g != 10);

		if (mult == 1000000000)
			outFile << "Case #" << i + 1 << ": " << forever << endl;
		else
			outFile << "Case #" << i + 1 << ": " << N << endl;

	}

	

	return 0;
}