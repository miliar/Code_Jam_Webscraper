#include <iostream>
#include <fstream>
#include <vector>
#define _INF 1000000

using namespace std;

int solve(vector<int>& p)
{
	int m = 0;
	for(int i = 0; i < p.size(); i++) {
		if(m < p[i]) {
			m = p[i];
		}
	}

	if(m == 0) return 0;

	vector< vector<int> > table;
	table.resize(m + 1);
	for(int i = 0; i <= m; i++) {
		table[i].resize(m + 1);
	}

	// index: pancake, time left
	for(int i = 0; i <= m; i++) {
		for(int j = 0; j <= m; j++) {
			if(i <= j) {
				table[i][j] = 0;
			}
			else {
				table[i][j] = _INF;
				for(int k = 1; k < i; k++) {
					if(k > j) break;

					if(table[i][j] > table[i - k][j] + 1) {
						table[i][j] = table[i - k][j] + 1;
					}
				}
			}
		}
	}

	int solution = _INF;
	for(int i = 0; i <= m; i++) {
		int count = i;
		for(int j = 0; j < p.size(); j++) {
			count += table[p[j]][i];
		}

		if(solution > count) {
			solution = count;
		}
	}

	return solution;
}


int main(int argc, char** argv)
{
	ifstream fin(argv[1]);
	int n;
	fin >> n;

	for(int i = 0; i < n; i++) {
		int d;
		vector<int> pancakes;
		fin >> d;

		pancakes.resize(d);
		for(int j = 0; j < d; j++) {
			fin >> pancakes[j];
		}

		cout << "Case #" << (i + 1) << ": " << solve(pancakes) << endl;
	}
	fin.close();
	return 0;
}