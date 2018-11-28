#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

#define MAXN 2000          /* How many vertices in U+V (in total) */

char e[MAXN][MAXN];       /* MODIFIED Adj. matrix (see note) */
int match[MAXN], back[MAXN], q[MAXN], tail;

void addEdge(int x, int y, int n) {
	e[x][y + n] = e[y + n][x] = 1;
}

int find(int x, int n, int m) {
	int i, j, r;

	if (match[x] != -1) return 0;
	memset(back, -1, sizeof(back));
	for (q[i = 0] = x, tail = 1; i < tail; i++)
		for (j = 0; j < n + m; j++) {
			if (!e[q[i]][j]) continue;
			if (match[j] != -1) {
				if (back[j] == -1) {
					back[j] = q[i];
					back[q[tail++] = match[j]] = j;
				}
			}
			else {
				match[match[q[i]] = j] = q[i];
				for (r = back[q[i]]; r != -1; r = back[back[r]])
					match[match[r] = back[r]] = r;
				return 1;
			}
		}
	return 0;
}

void bipmatch(int n, int m) {
	int i;
	memset(match, -1, sizeof(match));
	for (i = 0; i < n + m; i++) if (find(i, n, m)) i = 0;
}

int main() {
	string file = "C-large.in";
	ifstream input;
	input.open(file);
	ofstream output;
	output.open("out_" + file);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++)
	{
		output << "Case #" << cases << ": ";
		int l; input >> l;
		string a, b;
		map<string, int> left;
		map<string, int> right;

		memset(e, 0, sizeof(e));
		vector<vector<int> > e;

		for (int i = 0; i < l; i++) {
			input >> a >> b;
			if (left[a] == 0) {
				left[a] = left.size();
				e.push_back(vector<int>());
			}
			if (right[b] == 0)
				right[b] = right.size();
			e[left[a]-1].push_back(right[b]-1);
			//output << left[a] << right[b] << " ";
		}

		int n = left.size();
		int m = right.size();
		for (int i = 0; i < e.size(); i++) {
			for (int j = 0; j < e[i].size(); j++)
				addEdge(i, e[i][j], n);
		}
		bipmatch(n, m);

		int count = 0;
		for (int i = 0; i < n; i++) { 
			if (match[i] != -1) {
				//output << endl << i << " " << match[i] - n;
				count++;
			}
		}

		//output <<endl << n << " " << m << " " <<count << endl;
		output << l - (n + m - count) << endl;
	}
	output.close();
	input.close();
	return 0;
}