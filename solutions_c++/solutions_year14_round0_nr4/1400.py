#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <utility>
using namespace std;

ifstream fin ("D.in");
ofstream fout ("D.out");
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
#define pb push_back
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x)<0 ? -(x) : (x))

int main() {
	int T, c, n, i, j, war, dwar, bestK, lowK;
	fin >> T;
	vd N, K;
	for (c = 1; c <= T; c++) {
		fin >> n;
		N.resize(n, 0);
		K.resize(n, 0);
		for (i = 0; i < n; i++) fin >> N[i];
		for (i = 0; i < n; i++) fin >> K[i];
		sort(all(N));
		sort(all(K));

		war = n;
		j = 0;
		for (i = 0; i < n; i++) {
			for (; j < n; j++) {
				if (K[j] > N[i]) {
					war--;
					j++;
					break;
				}
			}
		}

		dwar = 0;
		lowK = 0;
		bestK = n-1;
		for (i = 0; i < n; i++) {
			if (N[i] > K[lowK]) {
				dwar++;
				lowK++;
			}
			else {
				bestK--;
			}
		}

		fout << "Case #" << c << ": " <<dwar << ' ' << war << endl;


		N.clear();
		K.clear();
	}
	return 0;
}
