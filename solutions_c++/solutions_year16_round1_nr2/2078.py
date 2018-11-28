#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
	ifstream ifile("txt.in");

	if (ifile.is_open()) {
		ofstream ofile("txt.out");
		string out = "";
		int test;
		ifile >> test;
		for (int i = 1; i <= test; ++i) {
			out += "Case #" + to_string(i) + ": ";
			int N;
			ifile >> N;
			vector<vector<int>> list;

			// Prise des données
			for (int j = 0; j < (2 * N) - 1; ++j) {
				vector<int> line;
				int height;
				for (int k = 0; k < N; ++k) {
					ifile >> height;
					line.push_back(height);
				}
				list.push_back(line);
			}
			int incomp;
			// Trie des données
			vector<vector<vector<int>>> data(N, vector<vector<int>>());
			for (int j = 0; j < N; j++) {
				int pos = 0;
				int pos2 = 0;
				for (int k = 1; k < list.size(); ++k) {
					if (list[k][j] < list[pos][j])
						pos = k;
					if (list[k][j] == list[pos][j])
						pos2 = k;
				}
				if (pos2 <= pos) {
					data[j].push_back(list[pos]);
					list.erase(list.begin() + pos);
					incomp = j;
				}
				else {
					data[j].push_back(list[pos]);
					data[j].push_back(list[pos2]);
					list.erase(list.begin() + pos);
					list.erase(list.begin() + pos2 - 1);
				}
			}

			// Construction de la liste manquante
			vector<int> m_list(N, 0);
			m_list[incomp] = data[incomp][0][incomp];
			for (int j = 0; j < N; ++j) {
				if (j != incomp) {
					if (data[j][0][incomp] == data[incomp][0][j]) {
						m_list[j] = data[j][1][incomp];
					}
					else {
						m_list[j] = data[j][0][incomp];
					}
				}
			}

			for (int j = 0; j < m_list.size(); ++j) {
				out += to_string(m_list[j]);
				if (j != m_list.size() - 1)
					out += ' ';
			}
			out += '\n';
		}

		ofile.clear();
		ofile << out;
		ofile.close();
		ifile.close();
	}

	return 0;
}