#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		int N,K;
		cin >> N >> K;
		vector<double> P(N);
		for(int i =0; i < N; i++) cin >> P[i];
		sort(begin(P),end(P));
		double ans =0;
		for(int i =0; i <= K; i++) {
			vector<double> p;
			for(int j =0; j < i; j++) p.push_back(P[j]);
			for(int j =N-1; j >= 0; j--) if(p.size() != K) p.push_back(P[j]);
			vector<double> D(K+1,0);
			D[0] =1;
			for(int j =0; j < K; j++) {
				vector<double> D_nw(K+1,0);
				for(int k =0; k <= K; k++) D_nw[k] +=D[k]*p[j];
				for(int k =0; k < K; k++) D_nw[k+1] +=D[k]*(1-p[j]);
				D =D_nw;}
			ans =max(ans,D[K/2]);}
		cout << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
