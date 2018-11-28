#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);

	int T; ifile >> T;
	for (int tc = 1; tc <= T; tc++) {
		int choice; 
		
		ifile >> choice;
		vector<int> first_nums;
		for (int r = 1; r <= 4; r++) {
			for (int i = 0; i < 4; i++) {
				int n; ifile >> n;
				if (r == choice) first_nums.push_back(n);
			}
		}

		ifile >> choice;
		vector<int> second_nums;
		for (int r = 1; r <= 4; r++) {
			for (int i = 0; i < 4; i++) {
				int n; ifile >> n;
				if (r == choice) second_nums.push_back(n);
			}
		}

		int common_nums = 0;
		int last_common = 0;
		for (int f = 0; f < first_nums.size(); f++) {
			for (int s = 0; s < second_nums.size(); s++) {
				if (first_nums[f] == second_nums[s]) {
					common_nums++;
					last_common = first_nums[f];
				}
			}
		}

		ofile << "Case #" << tc << ": ";
		if (common_nums == 0) ofile << "Volunteer cheated!";
		else if (common_nums == 1) ofile << last_common;
		else ofile << "Bad magician!";
		ofile << endl;
	}

	return 0;
}