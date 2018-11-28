#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long int Z;

Z S[1010101];
Z M[1010101];
Z A[1010101];
Z B[1010101];

Z mins, maxs;

int main() {
	cin.sync_with_stdio(false);
	
	Z Te;
	cin >> Te;
	for(Z T = 0; T < Te; ++T) {
		Z N, D;
		cin >> N >> D;
		
		Z As, Cs, Rs;
		Z Am, Cm, Rm;
		cin >> S[0] >> As >> Cs >> Rs;
		cin >> M[0] >> Am >> Cm >> Rm;
		
		for(Z i = 1; i < N; ++i) {
			S[i] = (S[i - 1] * As + Cs) % Rs;
			M[i] = (M[i - 1] * Am + Cm) % Rm;
		}
		
		for(Z i = 1; i < N; ++i) {
			M[i] %= i;
		}
		
		A[0] = S[0];
		B[0] = S[0];
		for(Z i = 1; i < N; ++i) {
			A[i] = min(S[i], A[M[i]]);
			B[i] = max(S[i], B[M[i]]);
		}
		
		map<Z, Z> E;
		for(Z i = 0; i < N; ++i) {
			Z in = B[i] - D;
			Z out = A[i] + 1;
			if(in < out) {
				++E[in];
				--E[out];
			}
		}
		auto it = E.begin();
		Z T1 = it->first - 5;
		it = E.end();
		--it;
		Z T2 = it->first + 5;
		T1 = min(T1, S[0] - D);
		T2 = max(T2, S[0]);
		
		Z jee = 0;
		Z cur = 0;
		for(Z t = T1; t <= T2; ++t) {
			cur += E[t];
			if(t >= S[0] - D && t <= S[0]) jee = max(jee, cur);
		}
		cout << "Case #" << T + 1 << ": " << jee << "\n";
	}
	
	return 0;
}
