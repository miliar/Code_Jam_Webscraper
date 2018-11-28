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
	int X;
	int R;
	int C;
	bool result;

public:
	Solver(char* fname_i_c) {
		this->fname_i = fname_i_c;
		this->fname_o = this->fname_i.substr(0, this->fname_i.find_last_of(".")) + ".out";
		ifstream ifs(this->fname_i);
		ofstream ofs(this->fname_o);

		ifs >> this->T;
		for (int No = 1; No <= this->T; No++){
			ofs << "Case #" << No << ": ";
			cout << "Case #" << No << ": ";
			this->read(ifs);
			this->result = this->calcurate();
			this->output(ofs);
		}
	}

private:
	void read(ifstream& ifs){
		ifs >> this->X >> this->R >> this->C;
		int minRC = min(this->R, this->C);
		int maxRC = max(this->R, this->C);
		this->C = maxRC;
		this->R = minRC;
	}

	void output(ofstream& ofs){
		if (this->result){
			ofs << "GABRIEL" << endl;
			cout << "GABRIEL" << endl;
		}
		else{
			ofs << "RICHARD" << endl;
			cout << "RICHARD" << endl;
		}
	}

	bool calcurate(){
		if (this->R * this->C % this->X != 0){
			return false;
		}

		if (this->X == 1){
			return true;
		}

		if (this->X == 2){
			return true;
		}

		if (this->X == 3){
			if (this->R == 1){
				return false;
			}
			else{
				return true;
			}
		}

		if (this->X == 4 && this->R <= 2){
			return false;
		}

		for (int row = 1; row < this->X; row++){
			if (this->X % row != 0) continue;
			int col = this->X / row;
			if (row > col) break;
			if ((row > this->R || col > this->C) && (row > this->C || col > this->R)){
				return false;
			}
		}

		return true;
	}
};

void main(int argc, char* argv[]){
	Solver* sol = new Solver(argv[1]);
	delete sol;
}
