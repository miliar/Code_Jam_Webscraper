
#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve(int t) {
	cout << "Case #"<< t<<": ";
	int N, X, res = 0;
	cin >> N >> X;
	vector<int> F(N);
	for(int i=0; i < N; i++) cin >> F[i];
	sort(F.rbegin(), F.rend());
	int f = 0, b = N-1;

	while(f <= b) {
		res++;
		if(F[f] + F[b] > X || f==b) {
			f++; 
		}
		else { f++; b--; }
	}

	cout << res << endl;
}
int main(void) {
	int T;
	cin >> T;

	for(int t=1;t<=T;t++) solve(t);
}