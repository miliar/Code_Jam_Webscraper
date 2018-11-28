#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

class Solver {
	int R;
	int C;
	int W;
	int A;

	void read(ifstream& ifs){
		ifs >> R >> C >> W;
	}

	void output(ofstream& ofs){
		ofs << A << endl;
		cout << A << endl;
	}

	void calcurate(){
		if (C % W == 0){
			A = (C / W) * (R - 1) + C / W + W - 1;
		}
		else{
			A = (C / W) * (R - 1) + C / W + W;
		}
	};

public:
	Solver(char* fname_i_c) {
		string fname_i = fname_i_c;
		string fname_o = fname_i.substr(0, fname_i.find_last_of(".")) + ".out";
		ifstream ifs(fname_i);
		ofstream ofs(fname_o);

		int T;
		ifs >> T;
		for (int No = 1; No <= T; No++){
			ofs << "Case #" << No << ": ";
			cout << "Case #" << No << ": ";
			read(ifs);
			calcurate();
			output(ofs);
		}
	}
};

void main(int argc, char* argv[]){
	Solver* sol = new Solver(argv[1]);
	delete sol;
}
