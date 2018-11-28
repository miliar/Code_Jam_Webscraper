#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <utility>
#include <sstream>
#include <string>
using namespace std;

ifstream fin ("C.in");
ofstream fout ("C.out");
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

ll powe(ll N, ll M) {
	ll res = 1;
	for (int i = 0; i < M; i++) res *= N;
	return res;
}

ll solve(vector<string> &S, ll i, ll N, ll M) {
	set<string> A;
	vector<ll> cod(M);
	ll tot = 0, j, k, l;
	for (j = 0; j < M; j++) {
		cod[j] = i % N;
		i /= N;
	}
	for (k = 0; k < N; k++) {
		A.clear();
		for (j = 0; j < M; j++) {
			if (cod[j] == k) {
				for (l = 0; l <= sz(S[j]); l++) A.insert(S[j].substr(0, l));
			}
		}
		tot += sz(A);
	}
	return tot;
}

int main() {
	ll T, c, N, M, i;
	vector<string> S;
	fin >> T;
	for (c = 1; c <= T; c++) {
		S.clear();
		fin >> M >> N;
		S.resize(M);
		for (i = 0; i < M; i++) fin >> S[i];
		ll res = 0, count;
		ll posres;
		for (i = 0; i < powe(N, M); i++) {
			posres = solve(S, i, N, M);
			if (res < posres) {
				res = posres;
				count = 0;
			}
			if (res == posres) count++;
		}
		fout << "Case #" << c << ": " << res << ' ' << count << endl;
	}


}
