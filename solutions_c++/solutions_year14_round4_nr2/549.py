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

ifstream fin ("B.in");
ofstream fout ("B.out");
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
	ll T, c, N, i, j, minA, minind;
	vll A;
	fin >> T;
	for (c = 1; c <= T; c++) {
		fin >> N;
		A.clear();
		A.resize(N);
		for (i = 0; i < N; i++) fin >> A[i];
		int res = 0;
		for (i = N; i > 0; i--) {
			minA = 1000000000000;
			for (j = 0; j < i; j++) {
				if (A[j] < minA) {
					minA = A[j];
					minind = j;
				}
			}
			res += min(minind, i - minind - 1);
			A.erase(A.begin() + minind);
		}

		fout << "Case #" << c << ": " << res << endl;
	}

	return 0;
}
