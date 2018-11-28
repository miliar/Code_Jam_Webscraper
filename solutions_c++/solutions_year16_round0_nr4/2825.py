#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

vector<unsigned int> compute_positions(unsigned int K, unsigned int C, unsigned int S) {
	
	// HINT: K = S
	vector<unsigned int> resultat;
	int debut;

	if(K == 1)

		debut = 1;

	else

		debut = 2;

	// Si on a C = 1 on lit l'artwork original
	if(C == 1) {
	
		for(int i = 1; i < K+1; i++) 

			resultat.push_back(i);

		return resultat;

	}

	else {
		resultat.push_back(debut);

		for(int i = 1; i < K-1; i++) {

			resultat.push_back(debut+K+i);

		}	

		return resultat;

	}

}

int main(int argc, char** argv) {

	ifstream my_file;
	my_file.open(argv[1]);

	int T, K, C, S;
	my_file >> T;

	int cas = 1;
	while(my_file >> K >> C >> S) {

		vector<unsigned int> result = compute_positions(K,C,S);

		cout << "Case #" << cas << ": ";
		for(int i = 0; i < result.size(); i++) 

			cout << result[i] << " ";

		cout << endl;
		cas++;

	}

	cout << endl;

	return 0;

}
