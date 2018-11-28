#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

class Solver {
	string fname_i;
	string fname_o;

	int T;
	int Smax;
	vector<int> Slv;
	int result;

public:
	Solver(char* fname_i_c) {
		this->fname_i = fname_i_c;
		this->fname_o = this->fname_i.substr(0, this->fname_i.find_last_of(".")) + ".out";
		ifstream ifs(this->fname_i);
		ofstream ofs(this->fname_o);

		ifs >> this->T;
		for (int No = 1; No <= this->T; No++){
			ofs << "Case #" << No << ": ";
			this->read(ifs);
			this->calcurate();
			this->output(ofs);
		}
	}

private:

	void read(ifstream& ifs){
		ifs >> this->Smax;
		this->Slv.resize(this->Smax + 1);
		char tmp;

		for (int ii = 0; ii <= this->Smax; ii++){
			ifs >> tmp;
			this->Slv[ii] = tmp - '0';
		}
	}

	void calcurate(){
		int sum = 0;
		this->result = 0;
		for (int ii = 0; ii <= this->Smax; ii++){
			if (sum + this->result < ii){
				this->result = ii - sum;
			}
			sum += this->Slv[ii];
		}
	}

	void output(ofstream& ofs){
		ofs << this->result << endl;
	}
};

void main(int argc, char* argv[]){
	Solver* sol = new Solver(argv[1]);
}
