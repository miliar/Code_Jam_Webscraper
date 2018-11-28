#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

double find_prob(vector<int> &pos, vector<double> &p, int k)
{
	double res = 0;
	for (int i=0;i<(1<<k);i++) {
		double val = 1;
		int votes = 0;
		for (int j=0;j<k;j++) {
			if ((i & (1 << j)) != 0) { 
				votes++;
				val *= p[pos[j]];
			}
			else {
				val *= (1.0 - p[pos[j]]);
			}
		}
		if (votes == k/2) {
			res += val;
		}
	}
	return res;
}

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	
	for (int q=0;q<z;q++) {
		int n,k;
		cin >> n >> k;
		vector<double> vals(n);
		for (int i=0;i<n;i++) {
			cin >> vals[i];
		}

		double best = -1;
		for (int i=1;i<(1<<n);i++) {
			vector<int> selected;
			for (int j=0;j<n;j++) {
				if ((i & (1 << j)) != 0) {
					selected.push_back(j);
				}
			}
			if (selected.size() != k) {
				continue;
			}
			double p = find_prob(selected, vals, k);
			if (p > best) {
				best = p;
			}
		}

		cout << "Case #" << (q + 1) << ": " << best << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}