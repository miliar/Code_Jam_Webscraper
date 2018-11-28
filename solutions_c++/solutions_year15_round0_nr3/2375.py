#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

class Solver {
	string fname_i;
	string fname_o;

	int T;
	long long int L;
	long long int X;
	map<string, string> table;
	string words;
	string target;
	string ijk = "ijk";
	int plusminus = 1;

	bool result;

public:
	Solver(char* fname_i_c) {
		this->fname_i = fname_i_c;
		this->fname_o = this->fname_i.substr(0, this->fname_i.find_last_of(".")) + ".out";
		ifstream ifs(this->fname_i);
		ofstream ofs(this->fname_o);

		this->words.reserve(20000);
		this->target.reserve(20000);

		this->table["ii"] = "";
		this->table["ij"] = "k";
		this->table["ik"] = "j";

		this->table["ji"] = "k";
		this->table["jj"] = "";
		this->table["jk"] = "i";

		this->table["ki"] = "j";
		this->table["kj"] = "i";
		this->table["kk"] = "";

		ifs >> this->T;
		for (int No = 1; No <= this->T; No++){
			ofs << "Case #" << No << ": ";
			cout << "Case #" << No << ": ";
			this->read(ifs);
			cout << this->target.length() << "\t";
			this->calcurate();
			this->output(ofs);
		}
	}

private:

	void read(ifstream& ifs){
		ifs >> this->L >> this->X;
		ifs >> this->words;
		this->target = "";
		this->plusminus = 1;
		while (this->addWords());
	}

	void output(ofstream& ofs){
		cout << this->target << "\t" << this->plusminus << "\t";
		if (this->result){
			ofs << "YES" << endl;
			cout << "YES" << endl;
		}
		else{
			ofs << "NO" << endl;
			cout << "NO" << endl;
		}
	}

	bool addWords(){
		if (this->X < 1) return false;
		this->target += this->words;
		this->X--;
		return true;
	}

	void flipPlusMinus(string word){
		if (word != "ij" && word != "jk" && word != "ki"){
			this->plusminus *= -1;
		}
	}

	void calcurate(){
		this->result = false;

		while (this->target[0] != 'i'){
			if (this->target.length() <= 3) break;
			string word = this->target.substr(0, 2);
			this->target.replace(0, 2, this->table[word]);
			this->flipPlusMinus(word);
		}

		if (this->target[0] != 'i'){
			return;
		}

		while (this->target[this->target.length() - 1] != 'k'){
			if (this->target.length() <= 3) break;
			string word = this->target.substr(this->target.length() - 2, 2);
			this->target.replace(this->target.length() - 2, 2, this->table[word]);
			this->flipPlusMinus(word);
		}

		if (this->target[this->target.length() - 1] != 'k'){
			return;
		}

		while (this->target.length() > 3){
			string word = this->target.substr(1, 2);
			this->target.replace(1, 2, this->table[word]);
			this->flipPlusMinus(word);
		}
		if (this->plusminus != 1 || this->target[1] != 'j'){
			return;
		}

		this->result = true;
	}
};

void main(int argc, char* argv[]){
//	Solver* sol = new Solver("C-small-attempt0.in");
	Solver* sol = new Solver(argv[1]);
	delete sol;
}
