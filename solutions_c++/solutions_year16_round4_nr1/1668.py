#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <map>
#include <unordered_map>
using namespace std;


struct sol_t {
	string R, P, S;
};

typedef tuple<int, int, int> i3;

map<i3, sol_t*> mem;

sol_t * solve(int R, int P, int S, int N) {
	if (mem.count(i3(R, P, S)) > 0) return mem[i3(R, P, S)];
	else {
		sol_t * sol = new sol_t;
		if (N == 1) {
			if (R == 1) sol->R = "R";
			else if (P == 1) sol->P = "P";
			else if (S == 1) sol->S = "S";
			else assert(false);
			
		} else for (int r0 = 0; r0 <= R; r0++) {
			for (int p0 = 0; p0 <= P; p0++) {
				int s0 = N / 2 - r0 - p0;
				if (s0 < 0 || s0 > S) continue;
				int r1 = R - r0, p1 = P - p0, s1 = S - s0;

				sol_t * l = solve(r0, p0, s0, N / 2);
				sol_t * r = solve(r1, p1, s1, N / 2);
				
				auto aux = [=](string &dst, string A0, string B0, string A1, string B1) {
					string newDst;
					if (A0.size() && B0.size()) newDst = A0 + B0;
					if (A1.size() && B1.size()) {
						string cand = A1 + B1;
						if (newDst.size() == 0) newDst = cand;
						else if (newDst.compare(cand) > 0) newDst = cand;
					}
					if (newDst.size() > 0) {
						if (dst.size() == 0) dst = newDst;
						else if (dst.compare(newDst) > 0) 
							dst = newDst;
					}
				};
				aux(sol->R, l->R, r->S, l->S, r->R);
				aux(sol->P, l->P, r->R, l->R, r->P);
				aux(sol->S, l->S, r->P, l->P, r->S);
			}
		}
		mem[i3(R, P, S)] = sol;
		return sol;
	}
}

int main(void) {
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {

		int R, P, S, N;
		cin >> N >> R >> P >> S;
		printf("Case #%i: ", t + 1);

		sol_t * sol = solve(R, P, S, 1 << N);
		string solStr;
		if (sol->R.size() && (sol->P.size() == 0 || sol->R.compare(sol->P) > 0) && (sol->S.size() == 0 || sol->R.compare(sol->S) > 0)) solStr = sol->R;
		else if (sol->P.size() && (sol->S.size() == 0 || sol->P.compare(sol->S) > 0)) solStr = sol->P;
		else solStr = sol->S;

		cout << (solStr.size() == 0 ? "IMPOSSIBLE" : solStr.c_str()) << endl;

		for (auto i : mem) delete i.second;
		mem.clear();
	}
	return 0;
}
