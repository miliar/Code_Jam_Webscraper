#include <bits/stdc++.h>
#define fst first
#define snd second
#define pb push_back
#define endl '\n'

using namespace std;


typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long int64;


int64 solve(int64 n) {
	if (n == 0) return -1LL;
	int64 cnt[10], ans = 0, cpy, mult = 1LL;
	fill(cnt, cnt + 10, 0);
	while (*min_element(cnt, cnt + 10) == 0) {
		cpy = n * mult;
		while (cpy) {
			cnt[cpy%10LL]++;
			cpy /= 10LL;
		}
		ans = n * mult;
		mult += 1LL;
	}
	return ans;
}

int main () {
	ifstream fin("in_a.in");
	ofstream fout("ans_a.out");
	int t;
	fin >> t;
	for (int num_case = 1; num_case <= t; num_case++) {
		int64 x; fin >> x;
		int64 ans = solve(x);
		fout << "Case #" << num_case << ": ";
		if (ans == -1LL) fout << "INSOMNIA\n";
		else fout << ans << endl;
	}
	return 0;
}