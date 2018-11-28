#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

class LessMoney {
public:

	int Compute(int c, int d, int v, vector<int> dm) {

		
		int ret = 0;
		for (int n = 1; n <= v; n++){
			if (!cando(n, dm)){
				dm.push_back(n);
				ret++;
			}
		}
		return ret;
	}

	bool cando(int a, vector<int> dm){
		for (int n = 1; n < (1 << dm.size()); n++){
			int num = 0;
			for (int m = 0; m < dm.size(); m++){

				if (n & (1 << m)) num += dm[m];
			}
			if (num == a) return true;
		}
		return false;
	}
};

int main(int argc, char *argv[]) {

	ifstream inFile("C:\\Users\\Mike\\Downloads\\C-small-attempt0.in");
	ofstream outFile("C:\\Users\\Mike\\Downloads\\C-small-attempt0.out");
	string line;
	getline(inFile, line);
	int cases;
	istringstream(line) >> cases;
	LessMoney proc;
	for (int n = 0; n < cases; n++){
		string nums;
		int c, d, v;
		getline(inFile, nums);
		istringstream iss(nums);
		iss >> c >> d >> v;
		vector<int> dm;
		getline(inFile, nums);
		istringstream iss2(nums);
		int tmp;
		for (int m = 0; m < d; m++){
			iss2 >> tmp;
			dm.push_back(tmp);
		}
		int ret = proc.Compute(c, d, v, dm);
		outFile << "Case #" << (n + 1) << ": " << ret << "\n";
	}
	return 0;
}

