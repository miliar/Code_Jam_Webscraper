#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

long long int gcd(long long int m, long long int n) {
	if (m == 0 || n == 0) return 0;

	while (m != n){
		if (m > n){
			m = m - n;
		}else{
			n = n - m;
		}
	}
	return m;
}

long long int lcm(long long int m, long long int n) {
	if (m == 0 || n == 0) return 0;
	return ((m / gcd(m, n)) * n);
}

class stM{
public:
	int No;
	long long int time;
	long long int numInLCM;
	long long int sum;

	bool operator <(const stM& target) {
		if (this->sum != target.sum){
			return this->sum < target.sum;
		}
		return this->No < target.No;
	}
};

class Solver {
	string fname_i;
	string fname_o;
	int result;

	int T;
	int B;
	long long int N;
	vector<stM> M;
	long long int leastCommonM;

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
		ifs >> this->B >> this->N;
		this->M.resize(this->B);
		for (int ii = 0; ii < B; ii++){
			ifs >> this->M[ii].time;
			this->M[ii].No = ii + 1;
			this->M[ii].numInLCM = 0;
			this->M[ii].sum = 0;
		}
	}

	void output(ofstream& ofs){
		ofs << result << endl;
		cout << result << endl;
	}

	void calcurate(){
		this->result = 0;

		this->leastCommonM = 1;
		for (auto& val : this->M){
			this->leastCommonM = lcm(this->leastCommonM, val.time);
		}

		long long int sum = 0;
		for (int ii = 0; ii < this->M.size(); ii++){
			this->M[ii].numInLCM = this->leastCommonM / this->M[ii].time;
			sum += this->M[ii].numInLCM;
		}

		this->N = this->N % sum;
		this->N = (this->N == 0) ? sum : this->N;

		sort(this->M.begin(), this->M.end());
//		this->checkM();
		while (this->N > 1){
			long long int a = this->M[0].sum;
			for (auto& m : this->M){
				m.sum -= a;
			}
			this->M[0].sum += this->M[0].time;
			sort(this->M.begin(), this->M.end());
			this->N--;
//			this->checkM();
		}

		this->result = this->M[0].No;
	}

	void checkM(){
		cout << "rest:" << this->N << endl;
		for (auto& m : this->M){
			cout << m.sum << "\t(" << m.No << "\t" << m.time << ")" << endl;
		}
		cout << "==========" << endl;
	}
};

void main(int argc, char* argv[]){
	
//	Solver* sol = new Solver("B-small-attempt0.in");
	Solver* sol = new Solver(argv[1]);
	delete sol;
}
