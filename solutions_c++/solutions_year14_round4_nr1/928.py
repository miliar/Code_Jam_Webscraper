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

ofstream fout ("2A.out");
ifstream fin ("2A.in");

int N,M;
int sizes[10005];

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		fin >> N >> M;
		for (int i = 0; i < N; i++) fin >> sizes[i];
		sort(sizes,sizes+N);
		int ans = 0;
		int l = 0;
		int r = N-1;
		while (l <= r) {
			if (sizes[r]+sizes[l] <= M) {
				ans++;
				l++;
				r--;
			}
			else {
				ans++;
				r--;
			}
		}
		fout << "Case #" << t << ": " << ans << "\n";
	}
    return 0;
}