#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	int t;
  	scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		int rows, cols;
		scanf("%d %d", &rows, &cols);
		vector<vector<int> > matrix;
		for (int i = 0; i < rows; i++) {
			matrix.push_back(vector<int>());
			for (int j = 0; j < cols; j++) {
				int a;
				scanf("%d", &a);
				matrix[i].push_back(a);
			}
		}

		while (true) {
			int k = 0;
			while (k < matrix.size()) {
				if (matrix[k].empty()) {
					matrix.erase(matrix.begin() + k);
					continue;
				}
				k++;
			}

			if (matrix.empty())
				break;

			int min = 1000000;
			int minr = 0;
			int minc = 0;
			for (int i = 0; i < matrix.size(); i++) {
				for (int j = 0; j < matrix[0].size(); j++) {
					if (matrix[i][j] < min) {
						min = matrix[i][j];
						minr = i;
						minc = j;
					}
				}
			}

			int numr = 0, numc = 0;
			bool re = true, ce = true;

			// check row
			for (int j = 0; j < matrix[minr].size(); j++) {
				if (matrix[minr][j] == min)
					numr++;
			}

			if (numr != matrix[minr].size())
				re = false;

			// check column
			for (int j = 0; j < matrix.size(); j++) {
				if (matrix[j][minc] == min)
					numc++;
			}

			if (numc != matrix.size())
				ce = false;

			if (!re && !ce) {
				printf("Case #%d: NO\n", c);
				break;
			}

			// clean column
			if (ce) {
				for (int j = 0; j < matrix.size(); j++) {
					matrix[j].erase(matrix[j].begin() + minc);
				}
			}
			// clean row
			else {
				for (int j = 0; j < matrix[minr].size(); j++) {
					matrix[minr].erase(matrix[minr].begin() + j);
				}
			}
		}

		if (matrix.size() > 0)
			continue;
    	printf("Case #%d: YES\n", c);
	}
	return 0;
}
