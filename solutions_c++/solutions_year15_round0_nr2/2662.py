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

ofstream fout ("QB.out");
ifstream fin ("QB.in");

int D,P[1005];

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		fin >> D;
		for (int i = 0; i < D; i++) fin >> P[i];
		int ans = 999999;
		for (int i = 1; i <= 1000; i++) {
			int cnt = 0;
			for (int j = 0; j < D; j++) cnt += (P[j]+i-1)/i-1;
			ans = min(ans,cnt+i);
		}
		fout << "Case #" << t << ": " << ans << "\n";
	}
    return 0;
}