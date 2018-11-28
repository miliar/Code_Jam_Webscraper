#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int N;
int BFF[1000];
bool used[1000];
vector<int> comb;
vector<int> data;

bool run_permut() {
	vector<int> temp(comb);
	bool check;
	sort(temp.begin(), temp.end());
	int check_first = temp[0];
	do {
		check = true;
		for (int i = 0; i < temp.size(); i++) {
			if (i == 0) {
				if (BFF[temp[i] - 1] != temp[temp.size() - 1] && BFF[temp[i] - 1] != temp[i + 1]) {
					check = false;
					break;
				}
			}
			else if (i == temp.size() - 1) {
				if (BFF[temp[i] - 1] != temp[i - 1] && BFF[temp[i] - 1] != temp[0]) {
					check = false;
					break;
				}
			}
			else {
				if (BFF[temp[i] - 1] != temp[i - 1] && BFF[temp[i] - 1] != temp[i + 1]) {
					check = false;
					break;
				}
			}
		}
		if (check)
			return true;
	} while (std::next_permutation(temp.begin(), temp.end()));
	return false;
}

bool try_combination(int off, int k) {
	if (k == 0)
		return run_permut();
	for (int i = off; i <= N - k; i++) {
		comb.push_back(i+1);
		if (try_combination(i + 1, k - 1))
			return true;
		comb.pop_back();
	}
	return false;
}

int run() {
	for (int i = N; i > 1; i--) {
		comb.clear();
		if (try_combination(0, i))
			return i;
	}
	return -1;
}

int main() {
	int T;
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		in >> N;
		for (int i = 0; i < N; i++)
			used[i] = false;
		for (int i = 0; i < N; i++) {
			in >> BFF[i];
			used[BFF[i] - 1] = true;
		}
		//read file
		int ret = run();
		//run
		//output
		out << "Case #" << t + 1 << ": " << ret << endl;
	}
	in.close();
	out.close();
	return 0;
}