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
	vector<int> numbers;
	int T;
	int N;

public:
	Solver(char* fname_i_c) {
		this->fname_i = fname_i_c;
		this->fname_o = this->fname_i.substr(0, this->fname_i.find_last_of(".")) + ".out";
		ifstream ifs(this->fname_i);
		ofstream ofs(this->fname_o);

		int maxN = 1000001;
		this->numbers.resize(maxN);
		for (int ii = 0; ii < maxN; ii++){
			this->numbers[ii] = maxN;
		}

		this->numbers[0] = 0;
		for (int ii = 1; ii < maxN; ii++){
			this->numbers[ii] = min(this->numbers[ii], this->numbers[ii - 1] + 1);

			int tmp = ii;
			while (tmp % 10 == 0){
				tmp = tmp / 10;
			}

			int tmp2 = 0;
			while (tmp > 0){
				int val = tmp % 10;
				tmp2 = tmp2 * 10 + val;
				tmp = tmp / 10;
			}
			this->numbers[tmp2] = min(this->numbers[tmp2], this->numbers[ii] + 1);
		}

		ifs >> this->T;
		for (int No = 1; No <= this->T; No++){
			ifs >> this->N;
			ofs << "Case #" << No << ": " << this->numbers[this->N] << endl;
			cout << "Case #" << No << ": " << this->numbers[this->N] << endl;
		}
	}
};

void main(int argc, char* argv[]){
	Solver* sol = new Solver(argv[1]);
	delete sol;
}
