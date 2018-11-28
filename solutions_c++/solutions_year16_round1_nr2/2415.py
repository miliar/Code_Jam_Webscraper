#include <iostream>
#include <string.h>
#include <stdint.h>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <bitset>
#include <assert.h>
using namespace std;

int N;
typedef vector<int> Seq;
vector<Seq> S;
map<int, Seq*> X;
map<int, Seq*> Y;
vector<int> C;
Seq R;

bool check(map<int, Seq*>& A, map<int, Seq*>& B)
{
#ifdef _DEBUG
	assert(A.size() == N);
	assert(B.size() == N - 1);
#endif
	//fill(C.begin(), C.end(), 0);

	auto itA = A.begin();
	for (int i = 0; i < N; i++) {
		Seq& s = *itA->second;
		for (int j = 0; j < N; j++) {
			C[i + j * N] = s[j];
		}
		++itA;
	}
	int skipped = -1;
	auto itB = B.begin();
	for (int i = 0; i < N; i++) {
		if (itB == B.end()) {
			if (skipped == -1) {
				skipped = i;
				continue;
			} else {
				return false;
			}
		}
		Seq& s = *itB->second;
		int* p = &C[i * N];
		if (s[0] != p[0]) {
			if (skipped == -1) {
				skipped = i;
				continue;
			} else {
				return false;
			}
		}
		for (int j = 1; j < N; j++) {
			if (s[j] != p[j]) {
				return false;
			}
		}
		++itB;
	}

	int* p = &C[skipped * N];
	for (int i = 0; i < N; i++) {
		R.push_back(p[i]);
	}
	return true;
}

bool solve(int i)
{
	if (i == S.size()) {
		if (Y.size() > X.size()) {
			return check(Y, X);
		} else {
			return check(X, Y);
		}
	}

	Seq& s = S[i];
	if (X.size() < N && X.find(s[0]) == X.end()) {
		X[s[0]] = &s;
		if (solve(i + 1)) {
			return true;
		}
		X.erase(s[0]);
	}
	if (Y.size() < N && Y.find(s[0]) == Y.end()) {
		Y[s[0]] = &s;
		if (solve(i + 1)) {
			return true;
		}
		Y.erase(s[0]);
	}
	return false;
}

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		S.clear();
		for (int i = 0; i < 2 * N - 1; i++) {
			vector<int> s(N);
			for (int j = 0; j < N; j++) {
				cin >> s[j];
			}
			S.push_back(move(s));
		}
		X.clear();
		Y.clear();
		C.resize(N * N);
		R.clear();
		solve(0);

		cout << "Case #" << i + 1 << ":";
		for (int r : R) {
			cout << " " << r;
		}
		cout << endl;
	}

	return 0;
}
