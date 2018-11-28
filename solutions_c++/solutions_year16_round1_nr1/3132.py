#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

string last_word(string word) {

	string reponse = "";

	reponse.push_back(word[0]);

	for(int i = 1; i < word.length(); i++) {

		int debut = 0;

		if(reponse[debut] <= word[i])

			reponse.insert(reponse.begin(), word[i]);

		else

			reponse.insert(reponse.end(), word[i]);

	}

	return reponse;
  
}

int main(int argc, char** argv) {

	ifstream my_file;
	my_file.open(argv[1]);

	int T;
	my_file >> T;

	int cpt = 0;

	string ligne="";
	getline(my_file, ligne);

	while(cpt < T) {

		ligne ="";
		getline(my_file, ligne);

		cout << "Case #" << (cpt+1) << ": " << last_word(ligne) << endl;	

		cpt++;

	}

	my_file.close();

	return 0;

}
