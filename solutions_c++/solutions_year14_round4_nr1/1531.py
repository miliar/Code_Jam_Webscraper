#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>

using namespace std;

ofstream fout ("Alarge.out");
ifstream fin ("Alarge.in");

int T;
int n,x,s[10010];

int main() {
	fin >> T;
	for (int tc = 1; tc <= T; tc++) {
		fin >> n >> x;
		for (int i = 0; i < n; i++) fin >> s[i];
		sort(s,s+n);
		int ans = 0;
		bool used[10010];
		memset(used,0,sizeof(used));
		for (int i = n-1; i >= 0; i--) {
			if (used[i]) continue;
			used[i] = 1;
			ans++;
			for (int l = i-1; l >= 0; l--) {
				if (!used[l] && s[l] + s[i] <= x) {
					used[l] = 1;
					break;
				}
			}
		}
		fout << "Case #" << tc << ": ";
		fout << ans << '\n';
	}
    return 0;
}