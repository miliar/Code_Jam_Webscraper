#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <utility>
#include <sstream>
using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
#define pb push_back
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x)<0 ? -(x) : (x))

int main() {
	int T, c, X, N, i, j;
	vi files;
	vi used;
	fin >> T;
	for (c = 1; c <= T; c++) {
		fin >> N >> X;
		files.clear();
		used.clear();
		files.resize(N);
		used.resize(N, 0);
		for (i = 0; i < N; i++) fin >> files[i];

		int res = 0;
		int left;
		sort(all(files));
		for (i = N-1; i >= 0; i--) {
			if (used[i] == 1) continue;
			left = X;
			res++;
			left -= files[i];
			used[i] = 1;
			for (j = i; j >= 0; j--) {
				if (used[j] == 0 && left >= files[j]) {
					used[j] = 1;
					break;
				}
			}

		}

		fout << "Case #" << c <<": " << res << endl;

	}

	return 0;
}
