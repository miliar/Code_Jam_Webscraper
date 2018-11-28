#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int main(){

	// Decleration
	ofstream fout ("war.out");
	ifstream fin ("war.in");

	int T, N, solution;
	vector<double> n;
	vector<double> k;

	fin >> T;
	for (int q = 0; q < T; q++){

		fin >> N;

		n.resize(N);
		k.resize(N);

		for(int i = 0; i < N; i++){
			fin >> n[i];
		}

		for(int i = 0; i < N; i++){
			fin >> k[i];
		}

		sort(n.begin(), n.end());
		sort(k.begin(), k.end());

		fout << "Case #" <<  q + 1 << ": ";

		solution = 0;

		for(int i = 0; i < N; i++){
			if(n[i] > k[solution]){
				solution++;
			}
		}
		fout << solution << " ";

		solution = N-1;

		for(int i = N-1; i >= 0; i--){
			if(n[i] < k[solution]){
				solution--;
			}
		}
		fout << solution + 1 << "\n";

	}

	return 0;
}