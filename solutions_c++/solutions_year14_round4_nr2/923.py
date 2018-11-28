#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

ofstream fout ("2B.out");
ifstream fin ("2B.in");

int N;
int inputs[1005];
pii ic[1005];
bool used[1005];

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		fin >> N;
		for (int i = 0; i < N; i++) fin >> inputs[i];
		for (int i = 0; i < N; i++) ic[i] = pii(inputs[i],i);
		for (int i = 0; i < N; i++) used[i] = false;
		sort(ic,ic+N);
		int ans = 0;
		int l = 0;
		int r = N-1;
		for (int i = 0; i < N; i++) {
			int lc = 0;
			int ind = 0;
			while (inputs[ind] != ic[i].first) {
				if (!used[ind]) lc++;
				ind++;
			}
			used[ind] = true;
			int rc = N-i-lc-1;
			if (lc < rc) {
				//l++;
				ans += lc;
			}
			else {
				//r--;
				ans += rc;
			}
		}
		fout << "Case #" << t << ": " << ans << "\n";
	}
    return 0;
}