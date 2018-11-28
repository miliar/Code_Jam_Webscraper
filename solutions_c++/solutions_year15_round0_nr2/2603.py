#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solver {
	string fname_i;
	string fname_o;

	int T;
	vector<int> P;
	vector<int> Pdiv;
	int time;

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
			this->calcurate();
			this->output(ofs);
		}
	}

private:
	void read(ifstream& ifs){
		int D;
		ifs >> D;
		this->P.resize(D);
		this->Pdiv.resize(D);

		for (int ii = 0; ii < D; ii++){
			ifs >> this->P[ii];
		}
	}

	int depthSearch(int posP, int divMax, int maxSize){
		if (this->P.size() <= posP){
			return maxSize;
		}
		if (this->P[posP] <= maxSize){
			return this->P[posP];
		}
		if (divMax == 0){
			return this->P[posP];
		}

		int result = 2000000;
		for (int divNum = 1; divNum <= divMax; divNum++){
			int divSize = this->P[posP] / (divNum + 1);
			divSize += (this->P[posP] % (divNum + 1) == 0) ? 0 : 1;
			int curMax = max(divSize, this->depthSearch(posP + 1, divMax - divNum, max(divSize, maxSize)));
			result = min(result, curMax);
		}
		return result;
	}

	void calcurate(){
		int divMax = 0;
		for (auto& val : this->P){
			divMax += val;
		}

		sort(this->P.begin(), this->P.end(), greater<int>());
		this->time = this->P[0];
		for (int divNum = 0; divNum <= divMax; divNum++){
			if (divNum > this->time) break;
			this->time = min(this->time, this->depthSearch(0, divNum, 0) + divNum);
		}
	}

	void output(ofstream& ofs){
		ofs << this->time << endl;
		cout << this->time << endl;
	}
};

void main(int argc, char* argv[]){
	Solver* sol = new Solver(argv[1]);
//	Solver* sol = new Solver("B-small-attempt0.in");
//	Solver* sol = new Solver("test2.in");
}
