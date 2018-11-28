#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

int main(int argc, char** argv) {

	ifstream my_file;
	ofstream output("output_B_large");

        my_file.open(argv[1]);

        int T;
        my_file >> T;
	int cpt = 1;
	int cas = 0;

	while(cas < T+1) {

		string ligne;
		getline(my_file, ligne);
		int alter = 0;

		if(cas >= 1) {
		output << "Case #" << cpt << ": ";

		for(int i = 0; i < ligne.length() - 1; i++) {

			if(ligne[i] != ligne[i+1])

				alter++;

		}

		if(ligne[ligne.length()-1] == '-') alter ++;

		output << alter << endl;
		cpt++;

		}
		cas++;

	}

	my_file.close();
	output.close();	

	return 0;

}
