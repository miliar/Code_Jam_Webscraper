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
		string S;
		int K;
		cin >> S >> K;
		int N =S.length();
		vector<int> A(N);
		for(int i =0; i < N; i++) A[i] =(S[i] == '+');
		int moves =0;

		if(A[0] == 0) {
			for(int i =0; i < K; i++) A[i] ^=1;
			moves++;}
		if(A[N-1] == 0) {
			for(int i =0; i < K; i++) A[N-1-i] ^=1;
			moves++;}

		vector<int> B(N-1);
		for(int i =0; i < N-1; i++) B[i] =A[i]^A[i+1];
		for(int i =0; i < N-1-K; i++) if(B[i]) {
			moves++;
			B[i] ^=1;
			B[i+K] ^=1;}
		for(int i =0; i < N-1; i++) if(B[i]) moves =-1;

		if(moves == -1) cout << "IMPOSSIBLE\n";
		else cout << moves << "\n";}
	return 0;}

// look at my code
// my code is amazing
