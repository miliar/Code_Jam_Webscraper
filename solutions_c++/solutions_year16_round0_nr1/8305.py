#include <iostream>
#include <vector>
#include <map>
#include <fstream>

using namespace std;

int out;
int main() {
	ifstream fin;
	 ofstream fout;

	 string inname, outname;
	 cin >> inname;
	 int iend = inname.rfind(".");
	 outname = inname.substr(0, iend) + ".out";

	 fin.open(inname);
	 fout.open(outname);
	 cin.rdbuf(fin.rdbuf());
	 cout.rdbuf(fout.rdbuf());

	int T, N;
	cin >> T;
	//cout << T << endl;
	int appear[10];
	int summe;

	summe = 0;

	for (int i = 0; i < T; i++) {
		//cout <<22222<<endl;
		cin >> N;
		//cout << N <<endl;
		if (N != 0) {
			int origin = N;

			for (int i = 0; i < 10; i++) {
					appear[i] = 0;
				}

			for(int j = 1, summe = 0; summe != 10; j++) {
				N = origin * j;
				//cout << "NN: "<<N<<endl;
				int rest = 0;
				while (N != 0) {
					rest = N % 10;
					N = N / 10;
					/*cout << "N: " << N <<endl;
					cout <<"rest: " << rest << endl;*/
					if (appear[rest] == 0) {
						appear[rest] = 1;
						if (summe == 9) {
							cout << "case #"<< i + 1<<": "<<origin * j << endl;
							summe++;
						} else {
							summe = summe + 1;
						}
					}
					//cout << summe << endl;

				}
			}

		}
		else {
			cout << "case #"<< i + 1<<": "<< "INSOMNIA" << endl;
		}

	}

	return 0;
}
