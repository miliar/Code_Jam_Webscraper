#include <fstream>
#include <string>
#include <vector>

using namespace std;

const vector<char> alfabeto{ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };

int posM(vector<int> P) {
	int max = 0, posMax = 0;
	for (int i = 0; i < P.size(); ++i) {
		if (P[i] > max) {
			max = P[i];
			posMax = i;
		}
	}

	return posMax;
}

int main() {
	ifstream archEnt;
	ofstream archSal;

	archEnt.open("entrada.txt");
	archSal.open("salida.out");

	int numVeces = 0;

	archEnt >> numVeces;

	for (int i = 0; i < numVeces; ++i) {
		int N = 0;
		bool acabado = false;
		bool par;
		archEnt >> N;
		par = !(N % 2);

		vector<int> P(N);

		archSal << "Case #" << i + 1 << ": ";

		for (int j = 0; j < N; ++j) {
			archEnt >> P[j];
		}
		string evacuar = "";
		int cont = 1;
		while (!acabado) {
			if (cont % 3 == 0)  {
				if (cont == 3) {
					archSal << evacuar;
					evacuar = "";
				}
				else {
					archSal << ' ' << evacuar;
					evacuar = "";
				}
				++cont;
			}
			else {
				int posMax = posM(P);
				if (P[posMax] == 0)
					acabado = true;
				else if (P[posMax] != 1) {
					--P[posMax];
					evacuar.push_back(alfabeto[posMax]);
				}
				else if (!par || (par && cont % 3 == 1)) {
					--P[posMax];
					evacuar.push_back(alfabeto[posMax]);
					par = !par;
				}
				++cont;
			}
		}
		archSal << '\n';
	}


	archEnt.close();
	archSal.close();
}