#include <fstream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

bool all_match(vector<string>);
int min_moves(vector<vector<int>>);

int main(int argc, char** argv) {
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);

	int T; ifile >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N; ifile >> N;

		vector<string> templates;
		vector<vector<int>> qtys;

		for (int n = 0; n < N; n++) {
			string str; ifile >> str;
			templates.push_back("");
			vector<int> v;
			qtys.push_back(v);

			templates[n].push_back(str[0]);
			qtys[n].push_back(1);

			for (int i = 1; i < str.size(); i++) {
				if (str[i] != str[i - 1]) {
					templates[n].push_back(str[i]);
					qtys[n].push_back(1);
				} else {
					qtys[n][qtys[n].size() - 1]++;
				}
			}
		}

		ofile << "Case #" << tc << ": ";
		if (!all_match(templates)) {
			ofile << "Fegla Won" << endl;
		} else {
			int min = min_moves(qtys);
			ofile << min << endl;
		}
	}

	return 0;
}

bool all_match(vector<string> strs) {
	for (int i = 1; i < strs.size(); i++) {
		if (strs[i].compare(strs[i - 1]) != 0) {
			return false;
		}
	}
	return true;
}

int min_moves(vector<vector<int>> nums) {
	vector<int> answer;

	int cols = nums[0].size();
	for (int c = 0; c < cols; c++) {
		int sum = 0;
		for (int r = 0; r < nums.size(); r++) {
			sum += nums[r][c];
		}
		float mean = round((float)sum / nums.size());
		answer.push_back(mean);
	}

	int min = 0;
	for (int r = 0; r < nums.size(); r++) {
		for (int c = 0; c < cols; c++) {
			min += abs(answer[c] - nums[r][c]);
		}
	}

	return min;
}