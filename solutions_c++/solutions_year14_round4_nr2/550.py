#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve(int t) {
	cout << "Case #"<< t<<": ";
	int N,res = 0, f = 0, l;
	cin >> N; l= N-1;
	vector<int> F(N), C(N);
	for(int i=0; i < N; i++){ cin >> F[i]; C[i] = F[i]; }

	sort(C.begin(), C.end());
	for(int i=0; i < N; i++) {
		for(int j=0; j < N; j++) {
			if(F[j] == C[i]) {
				if(j - f > l - j) {
					for(int k=j; k < l; k++) { swap(F[k], F[k+1]); res++; }
					l--;
				}
				else {
					for(int k=j-1; k >= f; k--) { swap(F[k], F[k+1]); res++; }
					f++;	
				}
				//cerr << f << " *** "<< l << endl;
				//for(int i=0; i < N; i++) cerr << F[i] << " " ; cerr << endl;
				break;
			}
		}
	}
	bool check  = false;
	//for(int i=0; i < N; i++) cerr << F[i] << endl;
	for(int i=0; i < N-1; i++) {
		if(F[i] < F[i+1] && !check) continue;
		if(F[i] < F[i+1] && check) { cerr << "ERROR "  << t <<endl; }
		check = true;
	}
	cout << res << endl;
}
int main(void) {
	int T;
	cin >> T;

	for(int t=1;t<=T;t++) solve(t);
}