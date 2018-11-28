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

ofstream fout ("QA.out");
ifstream fin ("QA.in");

int N;
string s;
int cnt[1005];

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		fin >> N >> s;
		for (int i = 0; i <= N; i++) {
			cnt[i] = s[i]-'0';
		}
		int ans = 0;
		int tot = 0;
		for (int i = 0; i <= N; i++) {
			if (tot < i) {ans++; tot++;}
			tot += cnt[i];
		}
		fout << "Case #" << t << ": " << ans << "\n";
	}
    return 0;
}