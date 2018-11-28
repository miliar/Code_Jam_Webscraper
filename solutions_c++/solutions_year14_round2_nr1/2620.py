#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Substring {
	char mander;
	int count;
};

typedef vector<Substring> String;

bool possible(const vector<String>& strings) {
	for (int i = 1; i < strings.size(); i++) {
		if (strings[i].size() != strings[0].size()) return false;
		for (int j = 0; j < strings[i].size(); j++) {
			if (strings[i][j].mander != strings[0][j].mander)
				return false;
		}
	}
	return true;
}

int main() {

ifstream ifs("inputA.txt");
if (ifs.is_open()) {
	ofstream ofs("outputA.txt");
	if (ofs.is_open()) {
		int T;
		ifs >> T;
		for (int i = 1;i <= T; i++) {
		int N;
		vector<String> strings;
		ifs >> N;
		for (int j = 0; j < N; j++) {
			string aux;
			ifs >> aux;
			String tmp;
			tmp.push_back({aux[0], 1});
			for (int i = 1;i< aux.size(); i++) {
				if (aux[i] == tmp[tmp.size()-1].mander)
				tmp[tmp.size()-1].count++;
				else
				tmp.push_back({aux[i], 1});
			}
			strings.push_back(tmp);
		}
		if (!possible(strings)) {
			ofs << "Case #" << i << ": Fegla Won" << endl;
		} else {
			vector<int> average;
			int avg;
			for (int k = 0; k < strings[0].size(); k++) {
				avg = 0;
				for (int l = 0; l < strings.size(); l++) {
					avg += strings[l][k].count;
				}
				avg /= strings.size();
				average.push_back(avg);
			}
			int total = 0;
			for (int k = 0; k < strings.size(); k++) {
				for (int l = 0; l < strings[k].size(); l++) {
					if (strings[k][l].count <= average[l]) {
						total += average[l] - strings[k][l].count;
					} else {
						total += strings[k][l].count - average[l];
					}
				}
			}
			ofs << "Case #" << i << ": " << total <<endl;	
		}
		}		
		ofs.close();
	}
	ifs.close();
}

return 0;
}