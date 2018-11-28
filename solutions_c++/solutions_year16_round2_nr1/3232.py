#include <iostream>
#include <fstream>
#include <string>
#include <vector>


#define Z 0
#define E 1
#define R 2
#define O 3
#define N 4
#define T 5
#define W 6
#define H 7
#define F 8
#define U 9
#define I 10
#define V 11
#define S 12
#define X 13
#define G 14


using namespace std;

int main(int argc, char** argv) {
	ifstream ifile("txt.in");

	if (ifile.is_open()) {
		string out = "";
		int test;
		ifile >> test;
		for (int i = 1; i <= test; ++i) {
			if (i == 94)
				int k = 0;
			out += "Case #" + to_string(i) + ": ";
			string input;
			ifile >> input;
			vector<int> letter(15);
			vector<int> c(10);

			for (int j = 0; j < input.length(); ++j) {
				switch (input[j]) {
				case 'Z':
					++letter[Z];
					break;
				case 'E':
					++letter[E];
					break;
				case 'R':
					++letter[R];
					break;
				case 'O':
					++letter[O];
					break;
				case 'N':
					++letter[N];
					break;
				case 'T':
					++letter[T];
					break;
				case 'W':
					++letter[W];
					break;
				case 'H':
					++letter[H];
					break;
				case 'F':
					++letter[F];
					break;
				case 'U':
					++letter[U];
					break;
				case 'I':
					++letter[I];
					break;
				case 'V':
					++letter[V];
					break;
				case 'S':
					++letter[S];
					break;
				case 'X':
					++letter[X];
					break;
				case 'G':
					++letter[G];
					break;
				}
			}

			// 1er degré
			for (int j = 0; j < input.length(); ++j) {
				switch (input[j]) {
				case 'Z':
					++c[0];
					--letter[Z];
					--letter[E];
					--letter[R];
					--letter[O];
					break;
				case 'W':
					++c[2];
					--letter[T];
					--letter[W];
					--letter[O];
					break;
				case 'U':
					++c[4];
					--letter[F];
					--letter[O];
					--letter[U];
					--letter[R];
					break;
				case 'X':
					++c[6];
					--letter[S];
					--letter[I];
					--letter[X];
					break;
				case 'G':
					++c[8];
					--letter[E];
					--letter[I];
					--letter[G];
					--letter[H];
					--letter[T];
					break;
				}
			}

			// 2e degré
			for (int j = 0; j < input.length(); ++j) {
				switch (input[j]) {
				case 'F':
					if (letter[F] > 0 && letter[I] > 0 && letter[V] > 0 && letter[E] > 0) {
						++c[5];
						--letter[F];
						--letter[I];
						--letter[V];
						--letter[E];
					}
					break;
				case 'S':
					if (letter[S] > 0 && letter[E] > 1 && letter[V] > 0 && letter[N] > 0) {
						++c[7];
						--letter[S];
						--letter[E];
						--letter[V];
						--letter[E];
						--letter[N];
					}
					break;
				case 'H':
					if (letter[T] > 0 && letter[H] > 0 && letter[R] > 0 && letter[E] > 1) {
						++c[3];
						--letter[T];
						--letter[H];
						--letter[R];
						--letter[E];
						--letter[E];
					}
					break;
				case 'O':
					if (letter[O] > 0 && letter[N] > 0 && letter[E] > 0) {
						++c[1];
						--letter[O];
						--letter[N];
						--letter[E];
					}
					break;
				}
			}

			// 3e degré
			for (int j = 0; j < input.length(); ++j) {
				if (input[j] == 'N' && letter[N] > 1 && letter[I] > 0 && letter[E] > 0) {
					++c[9];
					--letter[N];
					--letter[I];
					--letter[N];
					--letter[E];
				}
			}
			string d = "";
			// Construction de la sortie
			for (int j = 0; j < 10; ++j) {
				for (int k = 0; k < c[j]; ++k) {
					d += to_string(j);
				}
			}
			out += d;
			out += '\n';
		}

		ofstream ofile("txt.out");
		ofile.clear();
		ofile << out;
		ofile.close();
		ifile.close();
	}

	return 0;
}